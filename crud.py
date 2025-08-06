from models import Knowledge
from sqlalchemy.orm import Session

def create_knowledge(db: Session, knowledge_data):
    knowledge = Knowledge(**knowledge_data.dict())
    db.add(knowledge)
    db.commit()
    db.refresh(knowledge)
    return knowledge

def get_knowledges(db: Session):
    return db.query(Knowledge).all()
