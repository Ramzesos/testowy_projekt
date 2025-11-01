import os
from dotenv import load_dotenv

load_dotenv()  # wczyta zmienne z .env

def uruchom():
    app_name = os.getenv("APP_NAME", "Aplikacja domyślna")
    print(f"Startuję aplikację: {app_name}")
    print("Wersja developerska")