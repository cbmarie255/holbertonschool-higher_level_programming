#!/usr/bin/python3
"""
    A script that takes state as an arg and lists cities of that state.
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
                                SELECT cities.name FROM cities LEFT JOIN states
                                ON BINARY cities.state_id=states.id
                                WHERE states.name
                                LIKE %s ORDER BY cities.id ASC
                                ''', (args[4],))
    row_to_tuple = cursor_jawn.fetchall()
    output = ''
    for data in row_to_tuple:
        output += data[0] + ', '
    print(output[:-2])
