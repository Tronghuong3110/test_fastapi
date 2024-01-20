from fastapi import FastAPI

app = FastAPI()

@app.get("/hello", tags=["Root"])
async def hello():
    return {"message": "Xin chào mọi người!!"}