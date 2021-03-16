import re
import os
import sys
from Dialogs import *
import pyperclip as pc
# from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
import configparser as config
from cryptography.fernet import Fernet

################
# Window-Class #
################


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        ###################
        # Choose Database #
        ###################
        self.conf = config.ConfigParser()
        self.crypt = False
        try:
            open('Databases.conf', 'r', encoding='utf-8').close()
            self.conf.read('Databases.conf', encoding='utf-8')
            self.user = self.conf['DEFAULT']['USER']
        except FileNotFoundError:
            os.system("mkdir Databases")
            user = get_text(self, 'First start', 'Hello, you are starting this program\nfor the first time, '
                            'please enter your name.')
            self.user = user
            seed = Fernet.generate_key()
            pwd = self.encrypt(get_text(self, 'Password', 'Please enter your password', pw=True), seed)
            self.conf['DEFAULT'] = {'USER': user}
            name = get_text(self, 'Database', 'Please enter a Name for your Database')
            self.conf[user] = {
                'SEED': seed.decode('utf-8'),
                'PASSWORD': pwd,
                f'DATABASES': str([name])
            }
            db = config.ConfigParser()
            safe = get_bool(self, 'Secure?', 'Is this Database secured?')
            db['HEAD'] = {'NAME': name, 'Secured': safe}
            db['HEAD']['CODES'] = str("{}")
            if safe:
                db['HEAD']['PASSWORD'] = get_text(self, 'New Password', 'Enter a new Password', pw=True)
            else:
                db['HEAD']['PASSWORD'] = '--'
            with open('Databases.conf', 'w', encoding='utf-8') as e:
                self.conf.write(e)
            with open(f'Databases/{name}.conf', 'w', encoding='utf-8') as e:
                db.write(e)
            self.db_name = name

        i = 0
        msg = "Enter your Password: "
        while True:
            pw_temp = get_text(self, "Validate", msg, pw=True)
            if self.decrypt(self.conf[self.conf['DEFAULT']['USER']]['PASSWORD']) == pw_temp:
                break
            elif pw_temp == "<error_code>":
                sys.exit()
            else:
                i += 1
                msg = "Wrong Password: " + str(4-i)
                if i > 3:
                    sys.exit()
        self.open_db: config.ConfigParser() = config.ConfigParser()

        ######################
        # Item Configuration #
        ######################

        # New DB
        self.background = QLabel(self)
        self.cbDatabases = QComboBox(self)
        self.lUser = QLabel(self)
        self.pbAddBase = QPushButton(self)
        self.pbOpenBase = QPushButton(self)

        # Add Password
        self.lNmInput = QLabel(self)
        self.leNmInput = QLineEdit(self)
        self.lUsInput = QLabel(self)
        self.leUsInput = QLineEdit(self)
        self.lPwInput = QLabel(self)
        self.lePwInput = QLineEdit(self)
        self.progressbarStrength = QProgressBar(self)
        self.pbAddPw = QPushButton(self)

        # Show Data - Show Database
        self.lwDatabase = QListWidget(self)
        self.lNameOut = QLabel(self)
        self.leNameOut = QLineEdit(self)

        self.lPswOut = QLabel(self)
        self.lePswOut = QLineEdit(self)
        self.pbCopyPsw = QPushButton(self)
        self.pbCopyOpen = QPushButton(self)

        self.positioning()

        ########################
        # Window Configuration #
        ########################
        self.statusBar().showMessage(sys.version)
        self.setGeometry(100, 100, 1000, 550)
        self.setWindowTitle("Password Manager 1.0")
        self.setWindowIcon(QIcon("Logo.png"))
        self.background.setGeometry(0, 0, 1000, 550)
        self.background.setPixmap(QPixmap("Background.jpg"))
        self.show()

    ####################
    # Events and SLOTS #
    ####################

    def keyPressEvent(self, q_key_event):
        if q_key_event.key() == Qt.Key_Escape:
            sys.exit()
        elif q_key_event.key() == Qt.Key_I:
            self.debug_info()
        elif q_key_event.key() == Qt.Key_C:
            self.copy_pw()

    def new_base(self):
        db = config.ConfigParser()
        name = get_text(self, 'New Database Name', 'What is the name\nof your new Database.', pw=True)
        safe = get_bool(self, 'Secure?', 'Is this Database secured?')
        db['HEAD'] = {'NAME': name, 'Secured': safe}
        if safe:
            db['HEAD']['PASSWORD'] = self.encrypt(get_text(self, 'New Password', 'Enter a new Password', pw=True))
        else:
            db['HEAD']['PASSWORD'] = '--'
        db['HEAD']['CODES'] = str("{}")
        with open(f'Databases/{name}.conf', 'w', encoding='utf-8') as e:
            db.write(e)
        self.cbDatabases.addItem(name)
        self.conf[self.conf['DEFAULT']['USER']]['DATABASES'] = \
            str([self.cbDatabases.itemText(i) for i in range(self.cbDatabases.count())])
        with open('Databases.conf', 'w', encoding='utf-8') as e:
            self.conf.write(e)

    def open_base(self):
        self.lwDatabase.clear()
        db = config.ConfigParser()
        db_name = self.cbDatabases.currentText()
        db.read('Databases/'+db_name+".conf")
        if db['HEAD']['PASSWORD'] != "--":
            i = 0
            while not self.encrypt(get_text(self, "Password", "Please Enter the Database Password")) \
                    == db['HEAD']['PASSWORD']:
                i += 1
                if i > 3:
                    sys.exit()
        for row in eval(db['HEAD']['CODES']):
            self.lwDatabase.addItem(self.decrypt(row))
        self.db_name = db_name
        self.open_db = db
        self.pbAddPw.setVisible(True)

    def close_base(self):
        self.db_name = ''
        self.open_db = ''
        self.pbAddPw.setVisible(False)
        self.lwDatabase.clear()

    def add_pw(self):
        name = self.leNmInput.text()
        user = self.leUsInput.text()
        pswd = self.lePwInput.text()
        self.leNmInput.setText('')
        self.leUsInput.setText('')
        self.lePwInput.setText('')
        dic = eval(self.open_db['HEAD']['CODES'])
        dic[self.encrypt(name)] = [self.encrypt(user), self.encrypt(pswd)]
        self.open_db['HEAD']['CODES'] = str(dic)

        db_name = self.cbDatabases.currentText()
        with open(f'Databases/{db_name}.conf', 'w', encoding='utf-8') as e:
            self.open_db.write(e)
        self.open_base()

    def is_url(self):
        self.pbCopyOpen.setVisible(
            re.match(r"(w*\.|)[a-zA-Z0-9]+\.(com|de|net|gov)(/[a-zA-Z0-9]+|)", self.lwDatabase.currentItem().text())
            is not None)

    def copy_pw(self):
        pc.copy(self.lePswOut.text())
        self.lePswOut.setText('')

    def copy_open(self):
        self.copy_pw()
        os.system(f"start \"\" \"https://{self.leNameOut.text()}@{self.lwDatabase.currentItem().text()}\"")
        self.leNameOut.setText('')

    def password_strength(self):
        strength = 0
        password = self.lePwInput.text()
        if len(password) == 0:
            self.progressbarStrength.setValue(0)
            self.progressbarStrength.setFormat('')
            self.progressbarStrength.setStyleSheet("QProgressBar::chunk {background-color: red;}")
        elif len(password) > 10:
            strength += 40
        elif len(password) >= 5:
            strength += 20
            strength += (2*len(password))
        else:
            strength += (2*len(password))
        if re.search(r"[a-z]", password) is not None:
            strength += 10
        if re.search(r"[A-Z]", password) is not None:
            strength += 10
        if re.search(r"[0-9]", password) is not None:
            strength += 15
        if re.search(r"[^A-Za-z0-9]", password) is not None:
            strength += 15
        if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) is not None:
            strength += 10
        self.progressbarStrength.setValue(strength)
        if strength > 66:
            self.progressbarStrength.setFormat("Strong")
            self.progressbarStrength.setStyleSheet("QProgressBar::chunk {background-color: green;}")
        elif strength > 33:
            self.progressbarStrength.setFormat("Medium")
            self.progressbarStrength.setStyleSheet("QProgressBar::chunk {background-color: yellow;}")
        else:
            self.progressbarStrength.setFormat("Weak")
            self.progressbarStrength.setStyleSheet("QProgressBar::chunk {background-color: red;}")

    def show_data_from_widget(self):
        item = self.lwDatabase.currentItem().text()
        codes = eval(self.open_db['HEAD']['CODES'])
        clear = {}
        for code in codes:
            clear[self.decrypt(code)] = codes[code]
        pw_data = clear[item]
        temp = self.decrypt(pw_data[0])
        self.leNameOut.setText(temp)
        self.lePswOut.setText(self.decrypt(pw_data[1]))

    #############
    # Functions #
    #############

    def encrypt(self, text: str, seed=None):
        if self.crypt:
            return text
        if seed is None:
            seed = self.conf[self.user]['SEED']
            f = Fernet(bytes(seed, encoding='utf-8'))
        else:
            f = Fernet(seed)
        return f.encrypt(bytes(text, encoding='utf-8')).decode('utf-8')

    def decrypt(self, text: str, seed=None):
        if self.crypt:
            return text
        if seed is None:
            seed = self.conf[self.user]['SEED']
        f = Fernet(bytes(seed, encoding='utf-8'))
        temp = f.decrypt(bytes(text, encoding='utf-8')).decode('utf-8')
        return temp

    def positioning(self):
        self.lUser.setText(f"<h1>{str(self.conf['DEFAULT']['USER'])}</h1>")
        self.lUser.setGeometry(20, 10, 100, 30)
        self.lUser.setToolTip("The current user.")

        self.cbDatabases.addItems(eval(self.conf[self.conf['DEFAULT']['USER']]['DATABASES']))
        self.cbDatabases.setGeometry(20, 90, 100, 30)
        self.cbDatabases.setToolTip("ATTENTION: Closes the current Database.")
        self.cbDatabases.currentTextChanged.connect(self.close_base)

        self.pbAddBase.setGeometry(19, 50, 102, 30)
        self.pbAddBase.setText("Add Database")
        self.pbAddBase.setToolTip("WARNING: You can't transfer Passwords between Databases!")
        self.pbAddBase.clicked.connect(self.new_base)

        self.pbOpenBase.setGeometry(19, 130, 102, 30)
        self.pbOpenBase.setText("Open Database")
        self.pbOpenBase.clicked.connect(self.open_base)

        # Add Pw
        ########
        self.lNmInput.setGeometry(20, 220, 100, 30)
        self.lNmInput.setText("New entry name")
        self.leNmInput.setGeometry(20, 250, 100, 30)

        self.lUsInput.setGeometry(20, 290, 100, 30)
        self.lUsInput.setText("New entry Username")
        self.leUsInput.setGeometry(20, 320, 100, 30)

        self.lPwInput.setGeometry(20, 360, 100, 30)
        self.lPwInput.setText("New entry password")
        self.lePwInput.setGeometry(20, 390, 100, 30)
        self.lePwInput.textChanged.connect(self.password_strength)

        self.progressbarStrength.setGeometry(20, 425, 100, 30)
        self.progressbarStrength.setFormat("")
        self.progressbarStrength.setValue(0)

        self.pbAddPw.setGeometry(20, 460, 100, 30)
        self.pbAddPw.clicked.connect(self.add_pw)
        self.pbAddPw.setText("Add new entry")
        self.pbAddPw.setVisible(False)

        # Output
        ########
        self.lwDatabase.setGeometry(200, 20, 300, 500)
        self.lwDatabase.itemClicked.connect(self.show_data_from_widget)

        self.lNameOut.setText("Username")
        self.lNameOut.setGeometry(550, 20, 100, 30)
        self.leNameOut.setGeometry(550, 50, 140, 30)
        self.leNameOut.textChanged.connect(self.is_url)
        self.leNameOut.setReadOnly(True)

        self.lPswOut.setText("Password")
        self.lPswOut.setGeometry(550, 90, 100, 30)
        self.lePswOut.setGeometry(550, 120, 100, 30)
        self.lePswOut.setReadOnly(True)

        self.pbCopyPsw.setGeometry(655, 120, 35, 30)
        self.pbCopyPsw.setText("Copy")
        self.pbCopyPsw.clicked.connect(self.copy_pw)

        self.pbCopyOpen.setGeometry(550, 160, 140, 30)
        self.pbCopyOpen.setText("Copy and open Link")
        self.pbCopyOpen.clicked.connect(self.copy_open)
        self.pbCopyOpen.setVisible(False)

    def debug_info(self):
        print("--------------------------------------------------------------------")
        print("current meta data")
        print("Author: Nick")
        print("Python | Qt-Version: 3.8/3.9 | 5.13.")
        print(f"Version: {self.windowTitle()}")
        print("Datum: 16.03.2021")
        print("Tested on OS: Win 10")
        print("--------------------------------------------------------------------")


# MAIN_PROGRAM
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    print("2 - Window initialized")
    print("       __    __  ")
    print("      |  |__|  | ")
    print("      |___  ___| ")
    print("         |  |    ")
    print("         |  |    ")
    print("         |__|    ")
    sys.exit(app.exec_())
