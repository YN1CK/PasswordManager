from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def get_item(parent: QMainWindow, items: tuple = ('1', '2', '3'),
             title: str = "select from list", message: str = "list of Options"):

    item, ok = QInputDialog.getItem(parent, title, message, items, 0, False)

    if ok:
        return item
    else:
        return None


def get_text(parent: QMainWindow, title: str = 'Text Input', message: str = 'Enter your input:', pw: bool = False):
    if pw:
        text, ok = QInputDialog.getText(parent, title, message)
    else:
        text, ok = QInputDialog.getText(parent, title, message)

    if ok:
        return text
    else:
        return "<error_code>"


def get_int(parent: QMainWindow, title: str = "integer input dualog", message: str = "enter a number"):
    num, ok = QInputDialog.getInt(parent, title, message)

    if ok:
        return num
    else:
        return 0


def get_bool(parent: QMainWindow, title: str = "Title", message: str = "Message:"):
    return QMessageBox.Yes == QMessageBox.question(parent, title, message, QMessageBox.Yes, QMessageBox.No)
