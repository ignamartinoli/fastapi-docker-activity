from fastapi import FastAPI
import os

app = FastAPI()

APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from Dockerized FastAPI!")
DATA_DIR = os.getenv("DATA_DIR", "/data")


@app.get("/")
def root():
    return {"message": APP_MESSAGE, "data_dir": DATA_DIR}
