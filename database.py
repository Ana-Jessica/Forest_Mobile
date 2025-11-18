# database.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

# Nome do banco
db = client["estudos_app"]
