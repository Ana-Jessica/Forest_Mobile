# models/forest.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ForestSession(BaseModel):
    user_id: str = Field(..., example="ana123")
    nome_arvore: str = Field(..., example="Carvalho")
    minutos: int = Field(..., example=25)
    inicio: datetime = Field(..., example="2025-11-18T15:00:00Z")
    fim: Optional[datetime] = Field(None, example="2025-11-18T15:25:00Z")
    concluido: bool = Field(False, example=False)

class ForestSessionResponse(ForestSession):
    id: str
