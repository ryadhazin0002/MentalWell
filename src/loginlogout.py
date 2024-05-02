import sqlite3
from src.connect_to_database import DatabaseManager


class User:
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

class AuthenticationSystem:
    def __init__(self):
        self.logged_in_user = None
        self.connection = sqlite3.connect('MentalWell.db')
        self.cursor = self.connection.cursor()

    def register(self, name, username, password):
        self.cursor.execute('INSERT INTO users (name, username, password) VALUES (?, ?, ?)', (name, username, password))
        self.connection.commit()
        print("Registration successful.")

    def login(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = self.cursor.fetchone()
        if user:
            self.logged_in_user = User(user[0], user[1], user[2], user[3])
            print("Login successful.")
        else:
            print("Invalid username or password.")

    def logout(self):
        if self.logged_in_user:
            print(f"Logged out user: {self.logged_in_user.username}")
            self.logged_in_user = None
        else:
            print("No user logged in.")

    def __del__(self):
        self.connection.close()

# Usage
auth_system = AuthenticationSystem()

# Register a user
auth_system.register("John Doe", "johndoe", "password123")

# Login
def login_prompt():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    auth_system.login(username, password)

login_prompt()

# Logout (optional)
auth_system.logout()



