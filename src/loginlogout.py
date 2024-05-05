import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from login import Ui_Form  # Importera UI-klassen
from guestview import GuestView

class LoginLogic(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.guest_view = None

        self.ui.login.clicked.connect(self.login_handler)
        self.ui.signUp.clicked.connect(self.register_handler)
        self.ui.guest.clicked.connect(self.continue_as_guest_handler)

    def login_handler(self):
        username = self.ui.userName.text()
        password = self.ui.password.text()

    def register_handler(self):
        print("Sign Up button clicked!") 
        username = self.ui.userName.text()
        password = self.ui.password.text()
        
        print("Username:", username)
        print("Password:", password)

        if username and password:
            print("Both fields are filled.")
 
            QMessageBox.information(self, "Registration", "Registration successful!")
        else:
            print("One or both fields are empty.")
            QMessageBox.warning(self, "Registration", "Please enter both username and password.")

    def continue_as_guest_handler(self):
        if not self.guest_view:
            self.guest_view = GuestView()
        self.guest_view.show()

def main():
    app = QApplication(sys.argv)
    login_page = LoginLogic()
    login_page.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
