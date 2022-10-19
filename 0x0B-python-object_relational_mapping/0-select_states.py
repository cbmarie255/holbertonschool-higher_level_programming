#!/usr/bin/python3
"""
    A script that lists all states from the database hbtn_0e_0_usa.
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
    query = cursor_jawn.execute("SELECT * FROM states ORDER BY states.id")
    row_to_tuple = cursor_jawn.fetchall()
    for data in row_to_tuple:
        print(data)
