import os
import sys
import time

import psutil as ps
import sqlite3

DB_FILENAME = "system_metrics.db"


class Logger:
    def __init__(self):
        self.data_dict = {}

    def collect_data(self):
        '''collect data and assign to class variable'''
        self.data_dict['cpu'] = (int(time.time()), *ps.cpu_times())
        self.data_dict['vmemory'] = (int(time.time()), *ps.virtual_memory())

    def print_data(self, term_columns):
        print("-" * term_columns)
        print(f"UNIX Timestamp: {self.data_dict['cpu'][0]}")
        print("CPU TIME // User: {1:,.0f}, System: {3:,.0f}, Idle: {4:,.0f}".format(
            *self.data_dict['cpu'])
        )
        print("VIRT MEM // Total: {1:,d}, Available: {2:,d}".format(
            *self.data_dict['vmemory'])
        )

    def log_data(self):
        ''' log the data into sqlite database '''
        conn = sqlite3.connect(DB_FILENAME)
        cursor = conn.cursor()
        
        for table, data in self.data_dict.items():
            cnt = len(data)-1
            params = '?' + (',?' * cnt)

            cursor.executemany(f"INSERT INTO {table} VALUES({params})", (data,))
            conn.commit()

        conn.close()


def init_db() -> None:
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()

    with open('init_db.sql', 'r') as f:
        init_script = f.read()
        c.executescript(init_script)

    conn.commit()
    conn.close()


def main() -> None:
    init_db()

    while True:
        try:
            term_columns, term_len = os.get_terminal_size()

            logger = Logger()
            logger.collect_data()
            logger.print_data(term_columns)
            logger.log_data()
            time.sleep(30)

        except KeyboardInterrupt:
            print("Exiting manually...")
            sys.exit()

if __name__ == "__main__":
    main()

