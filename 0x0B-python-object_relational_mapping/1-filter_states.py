#!/usr/bin/python3
"""
    A script that lists all states with a name starting with N.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    args = argv
    username = args[1]
    password = args[2]
    db_name = args[3]
    data_base = MySQLdb.connect(host='localhost', user=username,
                                passwd=password, db=db_name,
                                port=3306)
    cursor_jawn = data_base.cursor()
    query = cursor_jawn.execute('''
                                SELECT * FROM states
                                WHERE states.name LIKE BINARY 'N%'
                                ORDER BY states.id ASC
                                ''')
    row_to_tuple = cursor_jawn.fetchall()
    for data in row_to_tuple:
        print(data)
