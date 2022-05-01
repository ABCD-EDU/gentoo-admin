from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/posts/{text}")
async def return_text(text: str) -> str:
        return {"text": text}
