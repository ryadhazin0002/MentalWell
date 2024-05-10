import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from login import Ui_Form  # Importera UI-klassen
from guest_view import GuestView
from connect_to_database import DatabaseManager  # Importera DatabaseManager

class LoginLogic(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.guest_view = None
        self.db_manager = DatabaseManager()  # Skapa en instans av DatabaseManager

        self.ui.login.clicked.connect(self.login_handler)
        self.ui.signUp.clicked.connect(self.register_handler)
        self.ui.guest.clicked.connect(self.continue_as_guest_handler)

    def login_handler(self):
        username = self.ui.userName.text()
        password = self.ui.password.text()
        # Implementera inloggningslogik här

    def register_handler(self):
        print("Connecting to database...")
        self.db_manager.connect()
        print("Connected to database!")
    
        username = self.ui.userName.text()
        password = self.ui.password.text()

        if username and password:
            if not self.db_manager.check_username_exists(username):
            # Om användarnamnet inte redan finns, spara det i databasen
                self.db_manager.execute_query(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
                QMessageBox.information(self, "Registration", "Registration successful!")
            else:
            # Om användarnamnet redan finns, visa varning
                QMessageBox.warning(self, "Registration", "Username already exists. Please choose a different username.")
        else:
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
