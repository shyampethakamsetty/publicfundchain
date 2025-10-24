
# Simple script to seed mock data into backend DB via FastAPI endpoints (example)
# Run after backend server is up
import requests, random, time

BASE = "http://127.0.0.1:8000/api"

beneficiaries = [
    {"name":"Asha", "aadhar":"xxxx-xxxx-0001", "region":"District A"},
    {"name":"Ravi", "aadhar":"xxxx-xxxx-0002", "region":"District B"},
    {"name":"Sita", "aadhar":"xxxx-xxxx-0003", "region":"District A"},
]

for i in range(10):
    payload = {
        "sender": "GovDept01",
        "receiver": random.choice(["Asha","Ravi","Sita"]),
        "amount": random.choice([500,1000,2000,5000]),
        "purpose": "Welfare"
    }
    r = requests.post(f"{BASE}/fund-transfer", json=payload)
    print(r.status_code, r.json())
    time.sleep(0.1)
