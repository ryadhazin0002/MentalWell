import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" MentalWell Web Browser")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        self.url_input = QLineEdit()
        self.layout.addWidget(self.url_input)

        self.load_url_button = QPushButton("Load URL")
        self.load_url_button.clicked.connect(self.load_url)
        self.layout.addWidget(self.load_url_button)

        self.load_iframe_button = QPushButton("Load Iframe")
        self.load_iframe_button.clicked.connect(self.load_iframe)
        self.layout.addWidget(self.load_iframe_button)

    def load_url(self):
        url = self.url_input.text()
        self.browser.setUrl(QUrl(url))

    def load_iframe(self):
        iframe_html = self.url_input.text()
        self.browser.setHtml(iframe_html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
