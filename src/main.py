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

@app.get("/get-users")
def get_users():
	cur = conn.cursor()
	data = get_all_users(cur)
	cur.close()
	return data

@app.get("/get-users/{qty}")
def get_users(qty):
	cur = conn.cursor()
	data = get_all_users_capped(cur, qty)
	cur.close()
	return data