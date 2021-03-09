#Imports
import sys
import os
import time
import secondary as sec
import Scramp as s
start_time = time.time()
build_time = -1
print("1--Import of passive Modules done")

print(sys.version)

from PyQt5.QtGui import *
from PyQt5.QtCore import *
print("2--Import from GtGui done")
from PyQt5.QtWidgets import *
print("3--Import from QtWidgets done")


#Class Application

class Window(QMainWindow):
    seed = "65168"
    #Var???
    pwd = open("password.gpf", "r")
    pal = pwd.readlines()
    pwd.close()
    print("4--List 1 was copied")
    usg = open("Usage.gpf", "r")
    tel = usg.readlines()
    usg.close()
    print("5--List 2 was copied")
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        #Normal Program
        a = 100
        self.lu = ""
        self.lp = ""


        QToolTip.setFont(QFont('Arial', 18))
        #QActions

        # Toolbar
        # ToolBar = self.addToolBar('Tooltest')
        # ToolBar.addAction(printtest)
        # Label
        bgpic = QLabel(self)
        bgpic.move(0, 0)
        bgpic.resize(1000, 550)
        bgpic.setPixmap(QPixmap("Hintergrund.jpg"))

        lab_head = QLabel(self)
        lab_head.move(440,20)
        lab_head.resize(130, 100)
        lab_head.setText('<h1>Passwörter</h1>')

        self.statusBar().showMessage('Klicke auf einen Button um das Passwort zu erhalten')


        # special Items
        closetime = QPushButton("Informationen", self)
        closetime.move(500, 100)
        closetime.clicked.connect(self.close_time)

        self.Show_Pass = QLabel(self)
        self.Show_Pass.move(500, 135)
        self.Show_Pass.setText("<Passwort wählen>")

        # Buttons
        psd = self.tel[0]
        psw1 = QPushButton(psd[:-1], self)
        psw1.move(100,150)
        psw1.clicked.connect(self.pass1)

        psd = self.tel[1]
        psw2 = QPushButton(psd[:-1], self)
        psw2.move(100,180)
        psw2.clicked.connect(self.pass2)

        psd = self.tel[2]
        psw3 = QPushButton(psd[:-1], self)
        psw3.move(100,210)
        psw3.clicked.connect(self.pass3)

        psd = self.tel[3]
        psw4 = QPushButton(psd[:-1], self)
        psw4.move(100, 240)
        psw4.clicked.connect(self.pass4)

        psd = self.tel[4]
        psw5 = QPushButton(psd[:-1], self)
        psw5.move(100, 270)
        psw5.clicked.connect(self.pass5)

        psd = self.tel[5]
        psw6 = QPushButton(psd[:-1], self)
        psw6.move(100, 300)
        psw6.clicked.connect(self.pass6)

        psd = self.tel[6]
        psw7 = QPushButton(psd[:-1], self)
        psw7.move(100, 330)
        psw7.clicked.connect(self.pass7)

        psd = self.tel[7]
        psw8 = QPushButton(psd[:-1], self)
        psw8.move(100, 360)
        psw8.clicked.connect(self.pass8)

        psd = self.tel[8]
        psw9 = QPushButton(psd[:-1], self)
        psw9.move(100, 390)
        psw9.clicked.connect(self.pass9)

        psd = self.tel[9]
        psw10 = QPushButton(psd[:-1], self)
        psw10.move(100, 420)
        psw10.clicked.connect(self.pass10)

        psd = self.tel[10]
        psw11 = QPushButton(psd[:-1], self)
        psw11.move(200, 150)
        psw11.clicked.connect(self.pass11)

        psd = self.tel[11]
        psw12 = QPushButton(psd[:-1], self)
        psw12.move(200, 180)
        psw12.clicked.connect(self.pass12)

        psd = self.tel[12]
        psw13 = QPushButton(psd[:-1], self)
        psw13.move(200, 210)
        psw13.clicked.connect(self.pass13)

        psd = self.tel[13]
        psw14 = QPushButton(psd[:-1], self)
        psw14.move(200, 240)
        psw14.clicked.connect(self.pass14)

        psd = self.tel[14]
        psw15 = QPushButton(psd[:-1], self)
        psw15.move(200, 270)
        psw15.clicked.connect(self.pass15)

        psd = self.tel[15]
        psw16 = QPushButton(psd[:-1], self)
        psw16.move(200, 300)
        psw16.clicked.connect(self.pass16)

        psd = self.tel[16]
        psw17 = QPushButton(psd[:-1], self)
        psw17.move(200, 330)
        psw17.clicked.connect(self.pass17)

        psd = self.tel[17]
        psw18 = QPushButton(psd[:-1], self)
        psw18.move(200, 360)
        psw18.clicked.connect(self.pass18)

        psd = self.tel[18]
        psw19 = QPushButton(psd[:-1], self)
        psw19.move(200, 390)
        psw19.clicked.connect(self.pass19)

        psd = self.tel[19]
        psw20 = QPushButton(psd[:-1], self)
        psw20.move(200, 420)
        psw20.clicked.connect(self.pass20)
        print("9--Buttons created")

        # Password Changer/setter
        mx = 500
        my = 200
        linp = QLabel(self)
        linp.setText("Paste Usage:")
        linp.move(mx, my)
        linp.resize(100, 25)
        self.inp = QLineEdit(self)
        self.inp.move(mx, my+30)
        self.inp.resize(100, 25)
        self.lpass = QLabel(self)
        self.lpass.setText("Passwort: ")
        self.lpass.move(mx, my+60)
        self.lpass.resize(100, 25)
        self.ipass = QLineEdit(self)
        self.ipass.move(mx, my+85)
        self.ipass.resize(100, 25)

        lslot = QLabel(self)
        lslot.setText("Slot eingeben: ")
        lslot.move(mx+110, my)
        lslot.resize(100, 25)
        self.islot = QLineEdit(self)
        self.islot.setValidator(QIntValidator())
        self.islot.move(mx+110, my+30)
        self.islot.resize(100, 25)
        self.islot.textChanged.connect(self.maxw)

        pbValidate = QPushButton(self)
        pbValidate.setText("Set Password")
        pbValidate.resize(100, 25)
        pbValidate.move(mx+110, my+85)
        pbValidate.clicked.connect(self.fillIn)

        # Password decrypter
        #self.Show_Pass.textChanged().connect(self.decrypt())

    # Window Declaration
        self.setGeometry(100,100,1000,550)
        self.setWindowTitle("Password Reminder")
        self.setWindowIcon(QIcon("Logo.png"))
        self.show()

        print("10--Window was created")
        global build_time
        build_time = time.time()-start_time
        print("--------------------------------------------------------------------")
        print("Build took "+str(time.time()-start_time)+" seconds.")
        print("--------------------------------------------------------------------")
        #Button Actions
    def decrypt(self):
        crypt = self.Show_Pass.Text()
        solved = s.crack(crypt, seed)
        self.Show_Pass.setText(solved)
    def maxw(self):
        if int(self.islot.text()) > 19:
            self.islot.setText("19")
        if self.islot.text() == "":
            self.islot.setText("0")
    def fillIn(self):
        sec.set(self.inp.text(), self.ipass.text(), int(self.islot.text()))

    def pass1(self):
        passw = self.pal[0]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass2(self):
        passw = self.pal[1]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass3(self):
        passw = self.pal[2]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass4(self):
        passw = self.pal[3]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass5(self):
        passw = self.pal[4]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass6(self):
        passw = self.pal[5]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass7(self):
        passw = self.pal[6]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass8(self):
        passw = self.pal[7]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass9(self):
        passw = self.pal[8]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass10(self):
        passw = self.pal[9]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass11(self):
        passw = self.pal[10]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass12(self):
        passw = self.pal[11]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass13(self):
        passw = self.pal[12]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass14(self):
        passw =  self.pal[13]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass15(self):
        passw = self.pal[14]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass16(self):
        passw = self.pal[15]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass17(self):
        passw = self.pal[16]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass18(self):
        passw =  self.pal[17]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass19(self):
        passw =  self.pal[18]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def pass20(self):
        passw =  self.pal[19]
        command = 'echo | set /p nul=' + passw.strip() + '| clip'
        os.system(command)
        print("Password in Clipboard: "+passw)
        self.Show_Pass.setText("PInClip")
    def close_time(self):
        self.Show_Pass.setText("""Autor: Yannick Reiß
Programmiert in: PyQt5, Python 3.6x86
Version: 2.2
Datum: 29.07.2020
OS: Windows (10); Linux Ubuntu (15)""")
        self.Show_Pass.resize(250, 65)
        print("--------------------------------------------------------------------")
        print("!!!Unfinished function")
        print("--------------------------------------------------------------------")
        print("Aktuell Programm- Daten")
        print("Autor: Yannick Reiß")
        print("Programmiert in: PyQt5, Python 3.6x86 ")
        print("Version: 2.2")
        print("Datum: 29.07.2020")
        print("Betriebssystem: Auf Win 10 und Linux Ubuntu 15.01 getestet.")
        print("--------------------------------------------------------------------")
    print("6--Functions created")
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            print("Program ended")
            sys.exit()
    print("7--You can now close the Window with 'ESC'")



# MAIN_PROGRAMM

#dispose trash
file = open("ext.bat", "w")
file.close()
os.system("del ext.bat")

print("8--Program called")
app = QApplication(sys.argv)
win = Window()
print("       __    __  ")
print("      |  |__|  | ")
print("      |___  ___| ")
print("         |  |    ")
print("         |  |    ")
print("         |__|    ")
print("Delay is: "+str(time.time()-build_time-start_time))

sys.exit(app.exec_())
