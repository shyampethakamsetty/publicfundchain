
import sqlite3
from pathlib import Path
import uuid, datetime, json

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "publicfundchain.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self._init()

    def _init(self):
        cur = self.conn.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS beneficiaries (
            id TEXT PRIMARY KEY,
            name TEXT,
            aadhar TEXT,
            region TEXT,
            total_received REAL DEFAULT 0
        )
        ''')
        cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            tx_id TEXT PRIMARY KEY,
            sender TEXT,
            receiver TEXT,
            amount REAL,
            purpose TEXT,
            timestamp TEXT,
            hash TEXT
        )
        ''')
        cur.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id TEXT PRIMARY KEY,
            tx_id TEXT,
            reason TEXT,
            severity TEXT,
            timestamp TEXT
        )
        ''')
        self.conn.commit()

    def create_transaction(self, tx):
        tx_id = f"TX{int(datetime.datetime.utcnow().timestamp())}{str(uuid.uuid4())[:6]}"
        tx_obj = {
            "tx_id": tx_id,
            "sender": tx['sender'],
            "receiver": tx['receiver'],
            "amount": tx['amount'],
            "purpose": tx.get('purpose',''),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "hash": ""
        }
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO transactions (tx_id, sender, receiver, amount, purpose, timestamp, hash)
                       VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (tx_obj['tx_id'], tx_obj['sender'], tx_obj['receiver'], tx_obj['amount'],
                     tx_obj['purpose'], tx_obj['timestamp'], tx_obj['hash']))
        self.conn.commit()
        return tx_obj

    def get_transactions(self):
        cur = self.conn.cursor()
        cur.execute('SELECT tx_id, sender, receiver, amount, purpose, timestamp, hash FROM transactions ORDER BY timestamp DESC')
        rows = cur.fetchall()
        cols = ['tx_id','sender','receiver','amount','purpose','timestamp','hash']
        return [dict(zip(cols, r)) for r in rows]

    def create_alert(self, tx_id, reason, severity):
        import uuid, datetime
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO alerts (id, tx_id, reason, severity, timestamp) VALUES (?, ?, ?, ?, ?)''',
                    (str(uuid.uuid4()), tx_id, reason, severity, datetime.datetime.utcnow().isoformat()))
        self.conn.commit()

    def get_alerts(self):
        cur = self.conn.cursor()
        cur.execute('SELECT id, tx_id, reason, severity, timestamp FROM alerts ORDER BY timestamp DESC')
        rows = cur.fetchall()
        cols = ['id','tx_id','reason','severity','timestamp']
        return [dict(zip(cols, r)) for r in rows]

    def summary(self):
        cur = self.conn.cursor()
        cur.execute('SELECT COUNT(*) FROM transactions')
        total = cur.fetchone()[0]
        cur.execute('SELECT COUNT(*) FROM alerts')
        alerts = cur.fetchone()[0]
        return {"total_transactions": total, "alerts": alerts}
