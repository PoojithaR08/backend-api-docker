from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/data")
def read_data():
    return {"data": {"id": 1, "name": "Sample JSON"}}
