# File used to process data from database

from time import sleep


def get_data2(text):
    return text

def get_data(cursor):
    cursor.execute("SELECT * FROM test_table")
    data = cursor.fetchone()

    return data

def fun1(cursor):
    cursor.execute("SELECT * FROM test_table")
    sleep(7)
    data = cursor.fetchone()
    print("data from fun1", data)
    return data

def fun2(cursor):
    cursor.execute("SELECT * FROM test_table")
    data = cursor.fetchall()
    print("i should be first", data)
    return data