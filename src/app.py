from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Testowy projekt API")

@app.get("/")
def root():
    app_name = os.getenv("APP_NAME", "Aplikacja domyślna")
    return {"message": f"Startuję: {app_name}"}

@app.get("/sum")
def sum_numbers(a: float, b: float):
    result = a + b
    return {"result": result}