# File used to connect to database

import psycopg2
from app.config import config

# TODO: Determine why path is relative to the file calling the method wtf lmao
params = config("config.ini", "postgresql")

def connect():
    conn = psycopg2.connect(**params)
    return conn

# Test database connectivity

# # Create cursor
# cur = conn.cursor()
# # Sample insert
# for i in range(10):
#     cur.execute("INSERT INTO test_table (column1,column2,column3) VALUES (%s,%s,%s);", [i,i,i])
# # Commit changes
# conn.commit()
# # Sample select
# cur.execute("SELECT * FROM test_table")
# returned = cur.fetchone()

# # close connection and curser
# cur.close()
# conn.close()
# # Output returned values
# print(returned)
# print(type(returned))
# print(type(cur))