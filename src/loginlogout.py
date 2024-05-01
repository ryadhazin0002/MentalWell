import sqlite3 
from src.connect_to_database import DatabaseManager


class User:
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    id: int
    name: str
    username: str
    password: str


class AuthenticationSystem:
    def __init__(self):
        self.logged_in_user = None
        self.connection = sqlite3.connect('MentalWell.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def register(self, email, password):
        self.cursor.execute('INSERT INTO users VALUES (?, ?)', (id, name, username, password))
        self.connection.commit()
        print("Registration successful.")

    def login(self, email, password):
        self.cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = self.cursor.fetchone()
        if user:
            self.logged_in_user = User(user[0], user[1])
            print("Login successful.")
        else:
            print("Invalid email or password.")

    def logout(self):
        if self.logged_in_user:
            print(f"Logged out user: {self.logged_in_user.email}")
            self.logged_in_user = None
        else:
            print("No user logged in.")

    def __del__(self):
        self.connection.close()

# Usage
auth_system = AuthenticationSystem()

# Register a user (you can add registration functionality if needed)
# auth_system.register("user@example.com", "password123")

# Login
def login_prompt():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    auth_system.login(email, password)

login_prompt()

# Logout (optional)
auth_system.logout()
