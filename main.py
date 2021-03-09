import sys
import os
import time
import secondary as sec
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

start_time = time.time()
print("1 - Import of Modules done")
print(sys.version)


################
# Window-Class #
################
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initMe()

        self.statusBar().showMessage('Klicke auf einen Button um das Passwort zu erhalten')

        self.setGeometry(100, 100, 1000, 550)
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
        solved = s.crack(crypt, self.seed)
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
