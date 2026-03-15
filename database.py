import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("attacks.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        attack_type TEXT,
        payload TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def log_attack(ip, attack_type, payload):
    conn = sqlite3.connect("attacks.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attacks (ip, attack_type, payload, timestamp)
    VALUES (?, ?, ?, ?)
    """, (ip, attack_type, payload, datetime.now()))

    conn.commit()
    conn.close()