
# Database Guide — Schema & Data Management

## Overview
Use SQLite for the hackathon for simplicity. This guide explains schema, seeding, and common queries.

## Schema (recommended)
- beneficiaries (id PK, name, aadhar, region, total_received)
- transactions (tx_id PK, sender, receiver, amount, purpose, timestamp, hash)
- alerts (id PK, tx_id FK, reason, severity, timestamp)

## Seeding data
- Use scripts/seed_data.py to POST sample transactions to `/api/fund-transfer`
- Ensure beneficiaries exist or create them on the fly when seeding

## Useful queries
- Recent transactions:
  `SELECT * FROM transactions ORDER BY timestamp DESC LIMIT 50;`
- Alerts count per region (join necessary):
  `SELECT b.region, COUNT(a.id) FROM alerts a JOIN transactions t ON a.tx_id=t.tx_id JOIN beneficiaries b ON t.receiver=b.name GROUP BY b.region;`

## Backups
- For demo, copy the SQLite DB file before big tests:
  `cp data/publicfundchain.db data/backup.db`
