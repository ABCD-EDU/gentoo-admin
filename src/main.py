from fastapi import FastAPI
from app.processing import get_data, get_data2
from app.connector import connect

app = FastAPI()

@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/posts/{text}")
async def return_text(text: str) -> str:
        return {"text": text}

@app.get("/get-data")
def get_datadb():
        conn = connect()
        cur = conn.cursor()
        data = get_data(cur)
        return data