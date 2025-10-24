
# Data Schema & Example Records

## beneficiaries (example)
- id: BENE001
- name: Asha
- aadhar: xxxx-xxxx-0001
- region: District A
- total_received: 1500.0

## transactions (example)
- tx_id: TX169...
- sender: GovDept01
- receiver: Asha
- amount: 500.0
- purpose: Education Aid
- timestamp: 2025-10-23T09:00:00Z
- hash: 0xabc123...

## alerts (example)
- id: UUID...
- tx_id: TX169...
- reason: "High transaction amount"
- severity: "High"
- timestamp: 2025-10-23T09:01:00Z
