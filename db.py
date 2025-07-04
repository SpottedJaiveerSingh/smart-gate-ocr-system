# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create table for residents (members/owners)
    c.execute('''
        CREATE TABLE IF NOT EXISTS residents (
            number TEXT PRIMARY KEY,
            name TEXT,
            flat TEXT
        )
    ''')

    # Create table for outsiders (visitors)
    c.execute('''
        CREATE TABLE IF NOT EXISTS outsiders (
            number TEXT,
            time_in TEXT,
            duration INTEGER,
            image_path TEXT
        )
    ''')

    conn.commit()
    conn.close()
def get_all_residents():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM residents")
    data = c.fetchall()
    conn.close()
    return data

def add_resident(number, name, flat):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO residents VALUES (?, ?, ?)", (number.upper(), name, flat))
    conn.commit()
    conn.close()

def delete_resident(number):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM residents WHERE number=?", (number.upper(),))
    conn.commit()
    conn.close()

def check_resident(number):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM residents WHERE number=?", (number.upper(),))
    result = c.fetchone()
    conn.close()
    return result

def log_outsider(number, time_in, duration, image_path):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO outsiders VALUES (?, ?, ?, ?)", 
              (number.upper(), time_in, duration, image_path))
    conn.commit()
    conn.close()


