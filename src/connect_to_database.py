import sqlite3

class DatabaseManager:
    _instance = None
    connection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'connection'):
            self.connection = None

    def connect(self):
        if self.connection is None:
            try:
                self.connection = sqlite3.connect('../MentalWell.db')
                print("Successfully Connected to SQLite")
            except sqlite3.Error as error:
                print("Error while connecting to a database:", error)

    def close(self):
        if self.connection:
            self.connection.close()
            print("SQLite connection is closed")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as error:
            print("Error executing query:", error)
            return None
        finally:
            cursor.close()