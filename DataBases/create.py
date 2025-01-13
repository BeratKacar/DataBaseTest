import sqlite3

#connect data
connection = sqlite3.connect("dataBase.db")

#create cursor
cursor = connection.cursor()

#create table
def create_data_base():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS numbers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number REAL NOT NULL,
            words REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()

print("Oluşturuldu")