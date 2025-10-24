
# AI Guide — Anomaly Detection (IsolationForest + Rules)

## Overview
This guide explains how to build the AI/ML pipeline for fraud detection using a hybrid approach: rule-based heuristics + IsolationForest anomaly detection.

## Data & Features
Collect transaction history and produce a feature matrix. Key features:
- `amount` (float)
- `time_gap_hours` (hours since last tx for same beneficiary)
- `tx_count_7d` (number of tx in last 7 days)
- `unique_ngos_received` (count of different NGOS sending to beneficiary)
- `region` encoded (one-hot or frequency encoding)
- `avg_amount_30d` (rolling avg)

## Steps

### 1) Offline data preparation & training (optional)
- Aggregate historical transactions into a CSV or DataFrame.
- Compute feature columns described above.
- Train IsolationForest:
  - `from sklearn.ensemble import IsolationForest`
  - Choose `contamination` conservatively (e.g., 0.02–0.05)
  - Fit on historical data excluding known frauds (if unavailable, use all data—model will still find outliers)

### 2) Model persistence
- After training, persist model using `joblib.dump(model, 'model.joblib')`
- Load in backend at startup `joblib.load('model.joblib')`

### 3) Online scoring (real-time checks)
- When a new transaction arrives:
  1. Compute feature vector for that transaction (requires access to recent history in DB)
  2. If a rule triggers (e.g., amount > threshold or duplicate aadhar), short-circuit and flag
  3. Else, feed feature vector to IsolationForest `model.score_samples([X])` and interpret score
  4. If score below threshold, create alert

### 4) Explainability
- Use simple rules to provide human-friendly reasons (e.g., 'high amount', 'duplicate aadhar')
- Optionally use `shap` to explain feature importance for anomaly decision (best effort in hackathon)

### 5) Evaluation (if you have labelled data)
- Compute precision/recall on labeled fraud examples
- Use confusion matrix to tune thresholds

### 6) Practical tips for hackathon
- Start with rules first — quick wins and explainable.
- Add IsolationForest later to surface subtle anomalies.
- Provide clear text reasons on the dashboard for every alert.
