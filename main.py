import sys
from PyQt5.QtWidgets import QApplication
from window import Window

# MAIN_PROGRAM
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    print("       __    __  ")
    print("      |  |__|  | ")
    print("      |___  ___| ")
    print("         |  |    ")
    print("         |  |    ")
    print("         |__|    ")
    sys.exit(app.exec_())
