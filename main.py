import os

from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtWidgets
from src.ui.menu import Ui_MainWindow
from config import database_path, music_path

print(database_path)
print(music_path)

#def main():
#    app = QApplication(sys.argv)
#    login_page = LoginLogic()
#    login_page.show()
#    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    menu = Ui_MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(menu)
    menu.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
