# 🏗️ PublicFundChain – Product Requirement Document (PRD)

## 🎯 Overview
**PublicFundChain** is a blockchain + AI-powered platform that ensures **transparency and accountability in welfare fund distribution**.  
It tracks every rupee allocated from government departments to NGOs to beneficiaries, providing a **tamper-proof ledger** and an **AI fraud detection engine**.

---

## 🧭 Vision
To build a **trustworthy, transparent, and intelligent welfare fund distribution system** using Blockchain for immutability and AI for fraud detection.

**Core Idea:** “Every rupee can be traced from the source to the beneficiary.”

---

## 🧩 Problem Statement
Government and NGO aid funds often suffer from **corruption, inefficiency, and data opacity**.  
Funds are lost due to fake beneficiaries, duplicate records, or intentional misreporting.

---

## 💡 Solution Summary
PublicFundChain introduces:
1. **Blockchain ledger** to track every transaction transparently.
2. **AI-powered fraud detection** to identify anomalies in distribution.
3. **Public dashboard** to visualize fund flow, anomalies, and program impact.

---

## ⚙️ System Architecture

### Architecture Layers
```
[React Frontend] ←→ [FastAPI Backend] ←→ [AI Engine (IsolationForest)]
                                 ↓
                        [Ganache Blockchain]
                                 ↓
                        [SQLite / Mock Dataset]
```

### Data Flow
1. Government allocates funds → recorded on blockchain.
2. AI model analyzes data for irregularities.
3. Backend exposes results via REST APIs.
4. React dashboard visualizes blockchain data and anomalies.

---

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| Frontend | React.js, Tailwind CSS | Interactive, modern UI |
| Visualization | Chart.js, Plotly.js | Graphs & data visualization |
| Backend | FastAPI (Python) | REST API, AI integration |
| Blockchain | Ganache (Ethereum Testnet), Solidity | Simulate fund ledger |
| AI Engine | scikit-learn (IsolationForest) | Fraud detection & anomaly analysis |
| Database | SQLite / JSON Mock Data | Store fund & alert data |
| API Integration | web3.py | Blockchain → Backend connectivity |
| Hosting | Vercel / Render / Replit | Cloud deployment for demo |

---

## 🧠 AI/ML Layer – Detailed Overview

### Goal
Detect fraudulent or suspicious transactions in real-time.

### Key Anomaly Types
- Duplicate beneficiaries (same Aadhar used multiple times)
- Irregular transaction frequency or amount
- NGOs routing funds unusually
- High geographic dispersion

### AI Workflow
```
[Transaction Data] → [Feature Engineering] → [Rule Engine] + [IsolationForest Model] → [Fraud Score + Alerts] → [Dashboard]
```

### Feature Examples
| Category | Feature | Purpose |
|-----------|----------|----------|
| Transaction | frequency, avg_amount, amount_variance | Detect misuse |
| Identity | unique_aadhar_count | Duplicate flag |
| Temporal | time_gap_between_tx | Burst detection |
| NGO | variance_in_fund_distribution | NGO bias |

### Model
**IsolationForest (scikit-learn)** – unsupervised anomaly detection model.  
Combines with **rule-based filters** for better accuracy.

---

## 🧰 Backend API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/transactions` | GET | Fetch all transactions |
| `/fund-transfer` | POST | Add a new fund transaction |
| `/anomalies` | GET | Return AI-detected anomalies |
| `/summary` | GET | Dashboard stats summary |

---

## 📊 Dashboard Modules (Frontend)

| Module | Description |
|---------|--------------|
| Fund Overview | Total allocated, disbursed, verified |
| Blockchain Explorer | All transactions with hash |
| Fraud Alerts | AI-detected anomalies |
| Beneficiary Insights | Filter by region/scheme |
| Geo Dashboard | Optional map-based fund visualization |

---

## 🔗 Blockchain Layer (Ganache + Solidity)

### Responsibilities
- Record transactions from government → NGO → beneficiaries
- Generate unique transaction hash
- Prevent data tampering
- Provide proof of delivery

### Sample Transaction Object
```json
{
  "tx_id": "TX20251001",
  "from": "GovDept01",
  "to": "Beneficiary123",
  "amount": 5000,
  "purpose": "Education Aid",
  "timestamp": "2025-10-23T09:00Z",
  "block_hash": "0xabc123..."
}
```

---

## 📦 Database Schema

### Table: beneficiaries
| Column | Type | Description |
|---------|------|--------------|
| id | INT | Unique ID |
| name | TEXT | Beneficiary name |
| aadhar | TEXT | Encrypted identifier |
| region | TEXT | Location |
| total_received | FLOAT | Total received funds |

### Table: transactions
| Column | Type | Description |
|---------|------|--------------|
| tx_id | TEXT | Transaction ID |
| from | TEXT | Sender |
| to | TEXT | Receiver |
| amount | FLOAT | Amount |
| timestamp | DATETIME | Time of transaction |
| hash | TEXT | Blockchain hash |

### Table: alerts
| Column | Type | Description |
|---------|------|--------------|
| tx_id | TEXT | Related transaction |
| reason | TEXT | Anomaly reason |
| severity | TEXT | Low / Medium / High |

---

## 🚀 Implementation Phases

| Phase | Focus | Deliverable |
|--------|--------|--------------|
| 1️⃣ | Setup Ganache, FastAPI, mock data | Working backend + blockchain |
| 2️⃣ | Integrate IsolationForest model | Fraud detection pipeline |
| 3️⃣ | React dashboard + APIs | Visualization |
| 4️⃣ | Testing + optimization | Demo-ready MVP |

---

## 🧩 MVP Scope (Hackathon Deliverables)

✅ Functional prototype with:
- Real-time blockchain transactions (Ganache)
- AI fraud detection (IsolationForest)
- Public dashboard with visual charts
- API connectivity and anomaly alerts

---

## 🧠 Future Roadmap

| Stage | Enhancement |
|--------|--------------|
| Phase 2 | Deploy on Polygon testnet |
| Phase 3 | Add geo-verification + citizen verification |
| Phase 4 | Voice/chatbot integration |
| Phase 5 | Real-time government data API integration |

---

## 🧭 Impact Summary

| Impact Area | Outcome |
|--------------|----------|
| Transparency | Verifiable, traceable welfare fund flow |
| Accountability | Reduced corruption and misuse |
| Trust | Citizens can track funds themselves |
| Scalability | Adaptable to any public distribution program |

---

## 📁 Repository Structure
```
/publicfundchain
│
├── /frontend        # React + Chart.js + Plotly UI
├── /backend         # FastAPI backend
├── /ai_engine       # IsolationForest + rule logic
├── /blockchain      # Ganache + Solidity contracts
├── /data            # Mock welfare datasets
└── /docs            # PRD, README, architecture diagrams
```

---

## 🧾 Summary Quote
> “PublicFundChain ensures every rupee reaches the right hand — transparently, intelligently, and verifiably.”
