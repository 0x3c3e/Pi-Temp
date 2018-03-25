import sqlite3

sqlite_path = '/home/pi/data/temperature.db'

def store(temperature):
    conn = sqlite3.connect(sqlite_path)
    curs = conn.cursor()
    try:
        curs.execute(
            """INSERT INTO temperatures VALUES(datetime('now','localtime'),(?))""", [temperature]
        )
    except:
        curs.execute("""CREATE TABLE temperatures (date DATETIME, temperature FLOAT)""")
    conn.commit()
    conn.close()


def get(date_from, date_to):
    conn = sqlite3.connect(sqlite_path)
    curs = conn.cursor()
    curs.execute("""SELECT * FROM temperatures WHERE date BETWEEN ? AND ?""", (date_from, date_to))
    temperatures = curs.fetchall()
    conn.close()
    return temperatures
