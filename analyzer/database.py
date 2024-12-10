import sqlite3

def init_db():
    conn = sqlite3.connect('packets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS packets
                 (src TEXT, dst TEXT, type TEXT, length INTEGER)''')
    conn.commit()
    conn.close()

def insert_packet(src, dst, packet_type, length):
    conn = sqlite3.connect('packets.db')
    c = conn.cursor()
    c.execute("INSERT INTO packets (src, dst, type, length) VALUES (?, ?, ?, ?)",
              (src, dst, packet_type, length))
    conn.commit()
    conn.close()

def get_all_packets():
    conn = sqlite3.connect('packets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM packets")
    rows = c.fetchall()
    conn.close()
    return rows
