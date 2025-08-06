from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Knowledge, Base

DB_URL = "mysql+pymysql://root:12345@localhost/pgila_db"

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            engine = create_engine(DB_URL)
            cls.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            Base.metadata.create_all(bind=engine)
            cls._instance = super(Database, cls).__new__(cls)
            
        return cls._instance

    def get_session(self):
        return self.SessionLocal()
