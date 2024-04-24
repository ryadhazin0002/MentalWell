# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resorces.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inspiring(object):
    def setupUi(self, inspiring):
        inspiring.setObjectName("inspiring")
        inspiring.resize(1000, 800)
        inspiring.setMinimumSize(QtCore.QSize(1000, 800))
        inspiring.setMaximumSize(QtCore.QSize(1000, 800))
        inspiring.setStyleSheet("background-color: rgb(47, 163, 209);")
        self.label = QtWidgets.QLabel(inspiring)
        self.label.setGeometry(QtCore.QRect(370, 70, 221, 191))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(inspiring)
        self.frame.setGeometry(QtCore.QRect(170, 320, 611, 331))
        self.frame.setStyleSheet("background-color: rgb(61, 220, 255);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(50, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.back.setObjectName("back")
        self.next = QtWidgets.QPushButton(self.frame)
        self.next.setGeometry(QtCore.QRect(230, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.next.setFont(font)
        self.next.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.next.setObjectName("next")
        self.mainMenu = QtWidgets.QPushButton(self.frame)
        self.mainMenu.setGeometry(QtCore.QRect(410, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mainMenu.setFont(font)
        self.mainMenu.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.mainMenu.setObjectName("mainMenu")
        self.resorces = QtWidgets.QLabel(self.frame)
        self.resorces.setGeometry(QtCore.QRect(70, 70, 471, 191))
        self.resorces.setStyleSheet("background-color: rgb(242, 217, 170);")
        self.resorces.setText("")
        self.resorces.setObjectName("resorces")
        self.author = QtWidgets.QLabel(self.frame)
        self.author.setGeometry(QtCore.QRect(410, 220, 121, 21))
        self.author.setStyleSheet("background-color: rgb(242, 217, 170);")
        self.author.setText("")
        self.author.setObjectName("author")

        self.retranslateUi(inspiring)
        QtCore.QMetaObject.connectSlotsByName(inspiring)

    def retranslateUi(self, inspiring):
        _translate = QtCore.QCoreApplication.translate
        inspiring.setWindowTitle(_translate("inspiring", "Form"))
        self.label_2.setText(_translate("inspiring", "External Resorces"))
        self.back.setText(_translate("inspiring", "Back"))
        self.next.setText(_translate("inspiring", "Next"))
        self.mainMenu.setText(_translate("inspiring", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inspiring = QtWidgets.QWidget()
    ui = Ui_inspiring()
    ui.setupUi(inspiring)
    inspiring.show()
    sys.exit(app.exec_())
