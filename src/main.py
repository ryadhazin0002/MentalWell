from PyQt5.QtWidgets import QApplication

import sys
from loginlogout import LoginLogic
from login import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

def main():
    app = QApplication(sys.argv)
    login_page = LoginLogic()
    login_page.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
