
# PublicFundChain - Hackathon Prototype Scaffold

This repository scaffold provides a working skeleton for the **PublicFundChain** project:
- React frontend (basic structure)
- FastAPI backend (endpoints + AI & blockchain hooks)
- Mock Solidity contract and Ganache notes
- Dockerfiles + docker-compose for local development
- Simple AI placeholder (IsolationForest) and mock ledger

> This scaffold is intended to accelerate your hackathon development. Fill in business logic, unit tests, and UI polish as needed.

## Quick start (development)
1. Start Ganache (UI) or run `ganache-cli` on port 8545.
2. Start backend (from `/backend`):
   ```bash
   cd backend
   pip install -r app/requirements.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
3. Start frontend (from `/frontend`):
   ```bash
   cd frontend
   npm install
   npm start
   ```

## Docker (demo)
You can use docker-compose to run the backend and frontend locally (Ganache must be available or mocked):
```bash
docker-compose up --build
```

