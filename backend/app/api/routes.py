
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.db import Database
from app.blockchain.ledger import Ledger
from app.ai.model import AnomalyEngine

router = APIRouter()
db = Database()
ledger = Ledger()
ai = AnomalyEngine()

class FundTransfer(BaseModel):
    sender: str
    receiver: str
    amount: float
    purpose: str

@router.get("/transactions")
def list_transactions():
    return db.get_transactions()

@router.post("/fund-transfer")
def fund_transfer(payload: FundTransfer):
    # Record in DB
    tx = db.create_transaction(dict(payload))
    # Write to blockchain
    blk = ledger.add_transaction(tx)
    # Run anomaly detection (async-able)
    alert = ai.check_transaction(tx)
    if alert:
        db.create_alert(tx['tx_id'], alert['reason'], alert['severity'])
    return {"tx": tx, "block": blk, "alert": alert}

@router.get("/anomalies")
def anomalies():
    return db.get_alerts()

@router.get("/summary")
def summary():
    return db.summary()
