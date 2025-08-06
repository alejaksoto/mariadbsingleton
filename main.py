from fastapi import FastAPI, Depends
from db_singleton import Database
from schemas import KnowledgeCreate, KnowledgeOut
from crud import create_knowledge, get_knowledges
from typing import List

app = FastAPI()
db_instance = Database()

def get_db():
    db = db_instance.get_session()
    try:
        yield db
    finally:
        db.close()

@app.post("/knowledges/", response_model=KnowledgeOut)
def add_knowledge(item: KnowledgeCreate, db=Depends(get_db)):
    return create_knowledge(db, item)

@app.get("/knowledges/", response_model=List[KnowledgeOut])
def list_knowledges(db=Depends(get_db)):
    return get_knowledges(db)
