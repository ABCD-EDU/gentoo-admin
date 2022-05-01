# File used to process data from database

def get_data2(text):
    return text

def get_data(cursor):
    cursor.execute("SELECT * FROM test_table")
    data = cursor.fetchone()
    cursor.close()
    return data
