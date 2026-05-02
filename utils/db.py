import sqlite3

def connect():
    return sqlite3.connect("database.db", check_same_thread=False)

def create_table():
    conn = connect()
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        party TEXT,
        count INTEGER
    )
    """)
    
    conn.commit()
    conn.close()


def add_vote(party):
    conn = connect()
    c = conn.cursor()
    
    c.execute("INSERT INTO votes (party, count) VALUES (?, ?)", (party, 1))
    
    conn.commit()
    conn.close()


def get_results():
    conn = connect()
    c = conn.cursor()
    
    data = c.execute("""
    SELECT party, SUM(count) 
    FROM votes 
    GROUP BY party
    """).fetchall()
    
    conn.close()
    return data


def reset_data():
    conn = connect()
    c = conn.cursor()
    
    c.execute("DELETE FROM votes")
    
    conn.commit()
    conn.close()
