from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/contract_analyzer")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Contract(Base):
    __tablename__ = "contracts"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    parties = Column(Text)  # JSON string
    dates = Column(Text)    # JSON string  
    values = Column(Text)   # JSON string
    created_at = Column(DateTime, nullable=False)
    processed_at = Column(DateTime)

# Criar tabelas
def create_tables():
    Base.metadata.create_all(bind=engine)