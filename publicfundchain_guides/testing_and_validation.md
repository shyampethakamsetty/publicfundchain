
# Testing & Validation Guide

## Unit Tests
- Backend routes: test `/api/fund-transfer`, `/api/transactions`, `/api/anomalies`
- DB layer: test create/get transactions and alerts
- AI engine: test rule-based flags and expected outputs

## Integration Tests
- Simulate end-to-end transaction: POST fund-transfer → ensure DB insert → ledger entry → alert creation (if expected)

## Manual Validation
- Seed dataset and verify charts in frontend match DB counts.
- Create known anomaly transactions (high amount or duplicate receiver) and confirm alerts.

## Performance
- For hackathon scope, target 100 TPS is unnecessary. Ensure app handles demo load (tens of requests/second).
