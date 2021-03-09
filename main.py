import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import configparser as config

start_time = time.time()
print("1 - Import of Modules done")
print(sys.version)


################
# Window-Class #
################
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        ###################
        # Choose Database #
        ###################
        items = {}
        conf = config.ConfigParser()
        try:
            open('Databases.conf', 'r').close()
            conf.read('Databases.conf')
        except FileNotFoundError:
            conf['BASES'] = {
                
            }

        ########################
        # Window Configuration #
        ########################
        self.statusBar().showMessage('Datenbank ist gesperrt')
        self.setGeometry(100, 100, 1000, 550)
        self.setWindowTitle("Password Manager 0.1")
        self.setWindowIcon(QIcon("Logo.png"))
        self.show()

    def get_item(self, items: list):
        item, ok = QInputDialog.getItem(self, 'Please choose an option', 'Choose an option from the list below',
                                        items, 0, False)
        if ok:
            return item
        else:
            return self.get_item(items)

    def debug_info(self):
        print("--------------------------------------------------------------------")
        print("Aktuelle Debug-Daten")
        print("Autor: Yannick Reiß")
        print("Programmiert mit: PyQt5, Python 3.8")
        print(f"Version: {self.windowTitle()}")
        print("Datum: 09.03.2021")
        print("Betriebssysteme: Win 10")
        print("--------------------------------------------------------------------")

    def keyPressEvent(self, q_key_event):
        if q_key_event.key() == Qt.Key_Escape:
            sys.exit()
        elif q_key_event.key() == Qt.Key_I:
            self.debug_info()


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
