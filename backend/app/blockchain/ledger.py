
import json
from web3 import Web3

# --- CONFIG (ACTION REQUIRED) ---
# 1. Deploy `contracts/Fund.sol` to Ganache using Remix IDE (see `blockchain_guide.md`).
# 2. Paste the deployed contract's address and ABI below.

GANACHE_URL = "http://127.0.0.1:8545"  # Default for ganache-cli. Use 7545 for Ganache UI.
CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS" # PASTE FROM REMIX
CONTRACT_ABI = """
PASTE_YOUR_ABI_JSON_HERE
"""
# --- END CONFIG ---

class Ledger:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
        if not self.w3.is_connected():
            raise ConnectionError(f"Failed to connect to Ganache at {GANACHE_URL}")
        
        if CONTRACT_ADDRESS == "YOUR_DEPLOYED_CONTRACT_ADDRESS" or not CONTRACT_ABI.strip():
            raise ValueError("Contract address and ABI have not been configured in ledger.py")

        self.contract = self.w3.eth.contract(
            address=self.w3.to_checksum_address(CONTRACT_ADDRESS),
            abi=json.loads(CONTRACT_ABI)
        )

    def add_transaction(self, tx_obj):
        """
        Records a transaction to the deployed FundLedger smart contract.
        """
        # Use the first Ganache account as the sender for the transaction.
        # In a real-world application, this would require secure private key management.
        owner_account = self.w3.eth.accounts[0]

        # Execute the `recordTransaction` function on the smart contract.
        tx_hash = self.contract.functions.recordTransaction(
            tx_obj['tx_id'],
            self.w3.to_checksum_address(owner_account), # Sender address
            tx_obj['receiver'], # Assuming receiver is a string; adapt if it's an address
            int(tx_obj['amount']),
            tx_obj['purpose']
        ).transact({'from': owner_account})

        # Wait for the transaction to be mined and get the receipt.
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        # Return the block hash and number as confirmation.
        return {
            "block_hash": receipt['blockHash'].hex(),
            "block_index": receipt['blockNumber']
        }

# Keep MockLedger for fallback or testing if needed, but it will not be used by default.
class MockLedger:
    def __init__(self):
        self.chain = []
        self._create_genesis()

    def _create_genesis(self):
        import time, hashlib
        genesis = {"index":0, "timestamp":time.time(), "data":"genesis", "prev_hash":"0", "hash":""}
        genesis['hash'] = self._hash_block(genesis)
        self.chain.append(genesis)

    def _hash_block(self, block):
        import hashlib
        block_str = json.dumps(block, sort_keys=True)
        return hashlib.sha256(block_str.encode()).hexdigest()

    def add_transaction(self, tx_obj):
        import time
        block = {
            "index": len(self.chain),
            "timestamp": time.time(),
            "data": tx_obj,
            "prev_hash": self.chain[-1]['hash']
        }
        block['hash'] = self._hash_block(block)
        self.chain.append(block)
        return {"block_index": block['index'], "block_hash": block['hash']}
