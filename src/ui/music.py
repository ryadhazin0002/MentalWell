# -*- coding: utf-8 -*-
import pygame.mixer
# Form implementation generated from reading ui file 'music.ui'
#
# Created by: PyQt5 ui code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from src.Track import TrackFunctions, Track
from src.music import MusicPlayer  # my code
from config import logo_path

music_player = MusicPlayer() # my code

class Ui_Music(object):

    def __init__(self, parent_page) -> None:
        super().__init__()
        self.functions = music_player.track_functions
        self.parent_page = parent_page
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
        self.label.setPixmap(QtGui.QPixmap(logo_path))
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
        font.setPointSize(14)
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
        #self.pushButton.setStyleSheet("QPushButton {\n"
        #                              "    background-color: #fdfcfa;\n"
        #                              "    border: 1px solid #0c253b;\n"
        #                              "    border-radius: 10px;\n"
        #                              "}\n"
        #                              "\n"
        #                              "QPushButton:pressed {\n"
        #                              "    /* Add styling for when the button is pressed */\n"
        #                              "    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
        #                              "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        #self.pushButton_2.setStyleSheet("QPushButton {\n"
        #                                "    background-color: #fdfcfa;\n"
        #                                "    border: 1px solid #0c253b;\n"
        #                                "    border-radius: 10px;\n"
        #                                "}\n"
        #                                "\n"
        #                                "QPushButton:pressed {\n"
        #                                "    /* Add styling for when the button is pressed */\n"
        #                                "    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
        #                                "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainMenu = QtWidgets.QPushButton(self.frame)
        def on_main_menu_clicked():
            if self.parent_page is not None:
                window = QtWidgets.QMainWindow()
                self.parent_page.setupUi(window)
                window.show()
                inspiring.close()


        self.MainMenu.clicked.connect(on_main_menu_clicked)
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
        self.list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.list_label.setStyleSheet("font-size: 24pt;")
        self.list_label.setStyleSheet("\n"
                                      "background-color: rgb(255, 170, 255);font-size: 24pt;")
        self.list_label.setText("")
        self.list_label.setObjectName("list_label")
        self.set_track(self.functions.current_track())

        self.retranslateUi(inspiring)
        self.button_functions()  # my code
        QtCore.QMetaObject.connectSlotsByName(inspiring)


    def retranslateUi(self, inspiring):
        _translate = QtCore.QCoreApplication.translate
        inspiring.setWindowTitle(_translate("inspiring", "Form"))
        self.label_2.setText(_translate("inspiring", "A list of Music"))
        #self.pushButton.setText(_translate("inspiring", "Back"))
        #self.pushButton_2.setText(_translate("inspiring", "Next"))
        self.MainMenu.setText(_translate("inspiring", "Main Menu"))
        self.prev_song_button.setText(_translate("inspiring", "|◁"))
        self.play_button.setText(_translate("inspiring", "▶ ılıılııl"))
        self.next_song_button.setText(_translate("inspiring", "▷|"))


    def button_functions(self):  # My code
        self.play_button.clicked.connect(music_player.play_logic)
        self.next_song_button.clicked.connect(self.on_next_pressed)
        self.prev_song_button.clicked.connect(self.on_back_pressed)



    def set_track(self, track: Track):
        if track != None:
            self.list_label.setText(f'{track.name}\n{track.author}')

    def on_next_pressed(self):
        track = self.functions.next_track()
        self.set_track(track)
        music_player.next_song()

    def on_back_pressed(self):
        track = self.functions.previous_track()
        self.set_track(track)
        music_player.prev_song()




if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    inspiring = QtWidgets.QWidget()
    ui = Ui_Music(None)
    ui.setupUi(inspiring)
    inspiring.show()
    sys.exit(app.exec_())
