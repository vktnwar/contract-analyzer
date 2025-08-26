from sqlalchemy.orm import Session
from .models import Contract, SessionLocal
from datetime import datetime
import json

def save_contract(filename: str, content: str, parties: list, dates: list, values: list):
    db = SessionLocal()
    try:
        contract = Contract(
            filename=filename,
            content=content,
            parties=json.dumps(parties),
            dates=json.dumps(dates),
            values=json.dumps(values),
            created_at=datetime.now(),
            processed_at=datetime.now()
        )
        db.add(contract)
        db.commit()
        return contract.id
    finally:
        db.close()

def get_all_contracts():
    db = SessionLocal()
    try:
        return db.query(Contract).all()
    finally:
        db.close()