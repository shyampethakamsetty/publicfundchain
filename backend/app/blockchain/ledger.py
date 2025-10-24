
import hashlib, json, time

class MockLedger:
    def __init__(self):
        self.chain = []
        self._create_genesis()

    def _create_genesis(self):
        genesis = {"index":0, "timestamp":time.time(), "data":"genesis", "prev_hash":"0", "hash":""}
        genesis['hash'] = self._hash_block(genesis)
        self.chain.append(genesis)

    def _hash_block(self, block):
        block_str = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_str.encode()).hexdigest()

    def add_transaction(self, tx_obj):
        block = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "data": tx_obj,
            "prev_hash": self.chain[-1]['hash']
        }
        block['hash'] = self._hash_block(block)
        self.chain.append(block)
        # Emulate returning blockchain hash
        return {"block_index": block['index'], "block_hash": block['hash']}
