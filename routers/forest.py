# routers/forest.py
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models.forest import ForestSession, ForestSessionResponse
from database import db
from utils.converters import doc_to_dict, id_to_objectid, docs_to_list
from bson.errors import InvalidId

router = APIRouter(prefix="/forest", tags=["Forest"])

collection = db["forest_sessions"]

@router.post("/", response_model=ForestSessionResponse, status_code=201)
def criar_sessao(sessao: ForestSession):
    payload = sessao.model_dump()
    result = collection.insert_one(payload)
    documento = collection.find_one({"_id": result.inserted_id})
    return doc_to_dict(documento)

@router.get("/", response_model=List[ForestSessionResponse])
def listar_sessoes(user_id: str = Query(..., description="ID do usuário (user_id)"),
                   skip: int = 0, limit: int = 100):
    """
    Lista sessões de um usuário (padrão: retorna até 100).
    Use skip & limit para paginação.
    """
    cursor = collection.find({"user_id": user_id}).skip(skip).limit(limit).sort("inicio", -1)
    docs = list(cursor)
    return docs_to_list(docs)

@router.get("/{id}", response_model=ForestSessionResponse)
def obter_sessao(id: str):
    try:
        doc = collection.find_one({"_id": id_to_objectid(id)})
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    if not doc:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")
    return doc_to_dict(doc)

@router.put("/{id}", response_model=ForestSessionResponse)
def atualizar_sessao(id: str, sessao: ForestSession):
    try:
        oid = id_to_objectid(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    payload = sessao.model_dump()
    result = collection.update_one({"_id": oid}, {"$set": payload})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")
    doc = collection.find_one({"_id": oid})
    return doc_to_dict(doc)

@router.delete("/{id}")
def deletar_sessao(id: str):
    try:
        oid = id_to_objectid(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    result = collection.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Sessão não encontrada")
    return {"mensagem": "Sessão deletada com sucesso"}
