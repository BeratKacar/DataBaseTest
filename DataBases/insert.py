import sqlite3
import random
import string

def create_random_number():
    return random.randint(0,100)

def create_random_words():
    return ''.join(chr(random.randint(0xAC00, 0xD7A3)) for _ in range(3))

def added_data():
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()

    number = create_random_number()
    words = create_random_words()

    cursor.execute("""
    INSERT INTO numbers (number, words)
    VALUES (?, ?)
    """, (number,words))

    connection.commit()
    connection.close()
    print(f"Data added: Number = {number}, Words = {words}")


if __name__ == "__main__":
    for _ in range(10):  # 10 rastgele veri ekle
        added_data()