# main.py
import os
from fastapi import FastAPI
from routers import forest
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="API Forest - Estudos",
    version="1.0",
    description="API para gerenciar sessões tipo 'Forest' (foco / pomodoro) por usuário."
)

# CORS — permite chamadas do app Android / web (ajuste conforme necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, restrinja para seus domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forest.router)

@app.get("/")
def root():
    return {"status": "API online", "version": "1.0"}
