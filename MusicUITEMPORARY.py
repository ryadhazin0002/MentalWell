import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from music import Music


# TODO connect music to the buttons

class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" MentalWell Web Browser")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        self.load_url_button = QPushButton("Play/Pause")
        self.load_url_button.clicked.connect(self.pause_play_button)
        self.layout.addWidget(self.load_url_button)

        self.load_url_button = QPushButton("Next")
        self.load_url_button.clicked.connect(self.previous_button)
        self.layout.addWidget(self.load_url_button)

        self.load_iframe_button = QPushButton("Previous")
        self.load_iframe_button.clicked.connect(self.next_button)
        self.layout.addWidget(self.load_iframe_button)

    def pause_play_button(self):
        pass

    def next_button(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaPlayer()
    window.show()
    sys.exit(app.exec_())
