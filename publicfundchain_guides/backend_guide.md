
# Backend Implementation Guide — FastAPI

## Overview
This guide walks through building the FastAPI backend that connects frontend, AI engine, and blockchain (Ganache).

## Project layout (backend/app)
```
/backend/app
├── main.py
├── api/
│   └── routes.py
├── db.py
├── blockchain/
│   └── ledger.py
├── ai/
│   └── model.py
└── requirements.txt
```

## Step-by-step

### 1) Setup environment
- Create virtualenv: `python -m venv venv && source venv/bin/activate`
- Install: `pip install -r app/requirements.txt`

### 2) Main app (app/main.py)
- Initialize FastAPI and CORS (already scaffolded).
- Mount API router under `/api`.

### 3) Database layer (db.py)
- Uses SQLite for quick prototyping.
- Functions required:
  - `create_transaction(tx)` — insert transaction and return tx object
  - `get_transactions()` — list transactions
  - `create_alert(tx_id, reason, severity)` — insert alert
  - `get_alerts()` — list alerts
  - `summary()` — return totals for dashboard

**Implementation tips:**
- Keep DB access synchronous for speed in hackathon; later use async if needed.
- Use parameterized queries to avoid SQL injection (even in mock).

### 4) API routes (api/routes.py)
Implement endpoints:
- `GET /api/transactions` → internal `db.get_transactions()`
- `POST /api/fund-transfer` →
  1. validate payload
  2. call `db.create_transaction(...)`
  3. write to blockchain ledger (`ledger.add_transaction(tx)`)
  4. call `ai.check_transaction(tx)`
  5. if alert, write alert into DB
  6. return {tx, block, alert}

- `GET /api/anomalies` → `db.get_alerts()`
- `GET /api/summary` → `db.summary()`

### 5) Blockchain integration (blockchain/ledger.py)
- For hackathon, start with mock ledger class that computes block hash and stores chain in memory (scaffold included).
- Later integrate `web3.py` to push transaction into Ganache smart contract.
- Design requirement: `add_transaction(tx_obj)` returns `{block_index, block_hash}` which you store in `transactions.hash` column.

### 6) AI integration (ai/model.py)
- Provide a small **AnomalyEngine** class exposing methods:
  - `fit(X)` — trains model (optional offline step)
  - `check_transaction(tx)` — returns `{reason, severity}` or `None`
- Start with hybrid rules + IsolationForest:
  1. Apply simple rules (high amount, duplicate aadhar etc.)
  2. If ML model available, compute feature vector and get anomaly score

### 7) Logging & Error handling
- Use Python `logging` module to log key events: new tx, blockchain write, AI alerts.
- Return HTTP 4xx/5xx appropriately for malformed payload/exception.

### 8) Local testing
- Run server: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- Use `curl` or Postman to call endpoints. Example:
```
curl -X POST http://127.0.0.1:8000/api/fund-transfer -H "Content-Type: application/json" -d '{"sender":"GovDept01","receiver":"Asha","amount":500,"purpose":"Education"}'
```

### 9) Next steps (nice-to-have)
- Add authentication for admin endpoints (JWT).
- Add background tasks for ML training (FastAPI background tasks).
- Add rate-limiting for public endpoints if deploying to demo server.
