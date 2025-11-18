# utils/converters.py
from bson.objectid import ObjectId
from typing import Dict, Any, List

def doc_to_dict(doc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converte documento Mongo (_id) para dicionário com campo 'id' string.
    """
    if doc is None:
        return None
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

def id_to_objectid(id_str: str) -> ObjectId:
    return ObjectId(id_str)

def docs_to_list(docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [doc_to_dict(d) for d in docs]
