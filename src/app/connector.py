# File used to connect to database

import psycopg2
from app.config import config

# read connection parameters
# TODO: Determine why path is relative to the file calling the method wtf lmao
# connect() is usually initially called from main.py (root/src/main.py)

def connect():
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        params = config("config.ini", "postgresql_gentoo_posts")
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	    # close the communication with the PostgreSQL
        cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def connect_users():
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        params = config("config.ini", "postgresql_gentoo_users")
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	    # close the communication with the PostgreSQL
        cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


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