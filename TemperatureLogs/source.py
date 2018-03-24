import glob
import time
import sqlite3

base_dir = '/sys/bus/w1/devices/'
sqlite_path = '/Users/a0x3c3e/data/temperature.db'


def read_temp_raw():
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def store(temperature):
    conn = sqlite3.connect(sqlite_path)
    curs = conn.cursor()
    try:
        curs.execute(
            """INSERT INTO temperatures VALUES(datetime(),(?))""", [temperature]
        )
    except:
        curs.execute("""CREATE TABLE temperatures (date DATETIME, temperature FLOAT)""")
    conn.commit()
    conn.close()


def get():
    conn = sqlite3.connect(sqlite_path)
    curs = conn.cursor()
    curs.execute("""SELECT * FROM temperatures""")
    temperatures = curs.fetchall()
    conn.close()
    return temperatures

if __name__ == "__main__":
    store(read_temp())