from PyQt5.QtWidgets import *


def get_item(parent: QMainWindow, items: tuple = ('1', '2', '3'),
             title: str = "select from list", message: str = "list of Options"):

    item, ok = QInputDialog.getItem(parent, title, message, items, 0, False)

    if ok:
        return item
    else:
        get_item(parent, items, title, message)


def get_text(parent: QMainWindow, title: str = 'Text Input Dialog', message: str = 'Enter your input:'):
    text, ok = QInputDialog.getText(parent, title, message)

    if ok:
        return text
    else:
        get_text(parent, title, message)


def get_int(parent: QMainWindow, title: str = "integer input dualog", message: str = "enter a number"):
    num, ok = QInputDialog.getInt(parent, title, message)

    if ok:
        return num
    else:
        get_int(parent, title, message)