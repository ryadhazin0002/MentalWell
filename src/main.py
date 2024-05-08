from PyQt5.QtWidgets import QApplication
import sys
from loginlogout import LoginLogic
from login import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from ui.menu import Ui_MainWindow


def main():
    app = QApplication(sys.argv)
    login_page = LoginLogic()
    login_page.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    menu = Ui_MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(menu)
    menu.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())