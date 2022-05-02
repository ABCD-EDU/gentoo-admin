from app.processing import *
from app.connector import connect

conn = connect()
cur = conn.cursor()
data = get_data(cur)

print(fun1(cur))
print(fun2(cur))