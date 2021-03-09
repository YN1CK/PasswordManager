from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.browser = QTextBrowser(self)
        self.resize(1000, 750)
        self.show()
        self.set_layout()

    def set_layout(self):
        self.browser.move(100, 100)
        self.browser.resize(100, 300)
        self.browser.setReadOnly(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    sys.exit(app.exec_())
