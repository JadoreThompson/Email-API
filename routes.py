from fastapi import FastAPI

app = FastAPI()

tasks = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

