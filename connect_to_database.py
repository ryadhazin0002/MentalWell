import sqlite3

try:
    sqliteConnection = sqlite3.connect('MentalWell.db')

    print("Successfully Connected to SQLite")

except sqlite3.Error as error:
    print("Error while connecting to a database", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
