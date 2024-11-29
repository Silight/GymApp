import sqlite3
import os

def database_connection():
    db_path = os.path.join(os.path.dirname(__file__), '../db/gym.db')
    conn = sqlite3.connect(db_path)
    return conn

def create_user_table():
    conn = database_connection()
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL, 
                age INTEGER NOT NULL,
                weight REAL NOT NULL,
                height REAL NOT NULL, 
                email TEXT NOT NULL,
                phone TEXT NOT NULL, 
                address TEXT NOT NULL, 
                notes TEXT
              )
              ''')
    conn.commit()
    conn.close()