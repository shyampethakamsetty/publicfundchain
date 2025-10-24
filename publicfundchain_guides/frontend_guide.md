
# Frontend Implementation Guide — React + Chart.js + Plotly

## Overview
Frontend visualizes transactions, anomalies, and overall stats, and allows triggering fund transfers (for demo).

## Project layout (frontend)
```
/frontend
├── public/index.html
├── src/
│   ├── App.jsx
│   ├── index.jsx
│   ├── components/
│   │   ├── Dashboard.jsx
│   │   ├── TransactionForm.jsx
│   │   └── Explorer.jsx
│   └── styles/
└── package.json
```

## Step-by-step

### 1) Setup
- Install dependencies: `npm install`
- Start dev server: `npm start` (runs on port 3000 by default)

### 2) Core components
- **Dashboard.jsx** — shows Fund Overview, Recent Transactions, Alerts.
- **TransactionForm.jsx** — simple form to POST `/api/fund-transfer` to simulate allocations.
- **Explorer.jsx** — shows blockchain explorer (list of blocks/transactions with hashes).

### 3) Data fetching
- Use `axios` to call backend endpoints. Endpoints are proxied via docker-compose / CORS allowed in backend.
- Example calls:
  - `GET /api/summary`
  - `GET /api/transactions`
  - `GET /api/anomalies`
  - `POST /api/fund-transfer`

### 4) Charts & Visuals
- Use **Chart.js** for simple bar/line charts via `react-chartjs-2` wrapper (optional).
- Use **Plotly.js** for interactive charts (time-series, heatmap).
- Suggested visual widgets:
  - Bar chart: Funds per scheme/NGO
  - Line chart: Disbursements over time
  - Heatmap: anomalies by region (or choropleth if you add GeoJSON)

### 5) UX considerations
- Keep UI minimal and readable — judges prefer clarity over fancy design.
- Show an **explainability panel** when an alert is clicked (why flagged).

### 6) Testing & Demo
- Seed data via `scripts/seed_data.py` or fixture file and refresh frontend.
- Ensure error handling (show messages if backend is offline).

### 7) Production hints
- Build frontend: `npm run build`
- Serve via Vercel or static server; configure CORS or host backend on same origin.
