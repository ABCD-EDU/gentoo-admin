from fastapi import FastAPI
from app.processing import *
from app.connector import connect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
conn = connect()

# ADD ADDRESS OF FRONTEND
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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