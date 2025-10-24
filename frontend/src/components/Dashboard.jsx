
import React, {useEffect, useState} from 'react';
import axios from 'axios';

export default function Dashboard(){
  const [summary, setSummary] = useState({total_transactions:0, alerts:0});
  const [transactions, setTransactions] = useState([]);
  const [anomalies, setAnomalies] = useState([]);

  useEffect(()=>{
    axios.get('/api/summary').then(r=>setSummary(r.data)).catch(()=>{});
    axios.get('/api/transactions').then(r=>setTransactions(r.data)).catch(()=>{});
    axios.get('/api/anomalies').then(r=>setAnomalies(r.data)).catch(()=>{});
  },[]);

  return (
    <div className="space-y-6">
      <section className="bg-white p-4 rounded shadow">
        <h2 className="text-xl font-medium">Fund Overview</h2>
        <div className="mt-2">
          <p>Total transactions: {summary.total_transactions}</p>
          <p>Alerts: {summary.alerts}</p>
        </div>
      </section>

      <section className="bg-white p-4 rounded shadow">
        <h2 className="text-xl">Recent Transactions</h2>
        <ul className="mt-2">
          {transactions.map(tx => (
            <li key={tx.tx_id} className="border-b py-2">
              {tx.tx_id} — {tx.sender} → {tx.receiver} — ₹{tx.amount}
            </li>
          ))}
        </ul>
      </section>

      <section className="bg-white p-4 rounded shadow">
        <h2 className="text-xl">Alerts</h2>
        <ul className="mt-2">
          {anomalies.map(a => (
            <li key={a.id} className="border-b py-2">
              {a.tx_id} — {a.reason} — {a.severity}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
