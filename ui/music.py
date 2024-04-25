# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
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
        self.label.setPixmap(QtGui.QPixmap("images/new_pic.png"))
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
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainMenu = QtWidgets.QPushButton(self.frame)
        self.MainMenu.setGeometry(QtCore.QRect(410, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MainMenu.setFont(font)
        self.MainMenu.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.MainMenu.setObjectName("MainMenu")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 471, 191))
        self.label_3.setStyleSheet("background-color: rgb(242, 217, 170);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.author = QtWidgets.QLabel(self.frame)
        self.author.setGeometry(QtCore.QRect(410, 220, 121, 21))
        self.author.setStyleSheet("background-color: rgb(242, 217, 170);")
        self.author.setText("")
        self.author.setObjectName("author")
        self.prev_song_button = QtWidgets.QPushButton(self.frame)
        self.prev_song_button.setGeometry(QtCore.QRect(120, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prev_song_button.setFont(font)
        self.prev_song_button.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.prev_song_button.setObjectName("prev_song_button")
        self.play_button = QtWidgets.QPushButton(self.frame)
        self.play_button.setGeometry(QtCore.QRect(244, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.play_button.setFont(font)
        self.play_button.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.play_button.setObjectName("play_button")
        self.next_song_button = QtWidgets.QPushButton(self.frame)
        self.next_song_button.setGeometry(QtCore.QRect(370, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.next_song_button.setFont(font)
        self.next_song_button.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.next_song_button.setObjectName("next_song_button")
        self.list_label = QtWidgets.QLabel(self.frame)
        self.list_label.setGeometry(QtCore.QRect(120, 90, 371, 101))
        self.list_label.setStyleSheet("\n"
"background-color: rgb(255, 170, 255);")
        self.list_label.setText("")
        self.list_label.setObjectName("list_label")

        self.retranslateUi(inspiring)
        QtCore.QMetaObject.connectSlotsByName(inspiring)

    def retranslateUi(self, inspiring):
        _translate = QtCore.QCoreApplication.translate
        inspiring.setWindowTitle(_translate("inspiring", "Form"))
        self.label_2.setText(_translate("inspiring", "A list of Music"))
        self.pushButton.setText(_translate("inspiring", "Back"))
        self.pushButton_2.setText(_translate("inspiring", "Next"))
        self.MainMenu.setText(_translate("inspiring", "Main Menu"))
        self.prev_song_button.setText(_translate("inspiring", "|◁"))
        self.play_button.setText(_translate("inspiring", "▶ ılıılııl"))
        self.next_song_button.setText(_translate("inspiring", "▷|"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inspiring = QtWidgets.QWidget()
    ui = Ui_inspiring()
    ui.setupUi(inspiring)
    inspiring.show()
    sys.exit(app.exec_())
