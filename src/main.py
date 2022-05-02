from fastapi import FastAPI
from app.processing import *
from app.connector import connect

app = FastAPI()
conn = connect()

@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/posts/{text}")
async def return_text(text: str) -> str:
        return {"text": text}

@app.get("/get-data")
def get_datadb():
        cur = conn.cursor()
        data = get_data(cur)
        cur.close()
        return data

@app.get("/fun1")
def get_datadb():
        cur = conn.cursor()
        data = fun1(cur)
        cur.close()
        return data

@app.get("/fun2")
def get_datadb():
        cur = conn.cursor()
        data = fun2(cur)
        cur.close()
        return data