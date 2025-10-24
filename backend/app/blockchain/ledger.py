
import json
from web3 import Web3

class Ledger:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider('http://0.0.0.1:8545'))
        if not self.w3.is_connected():
            raise Exception("Failed to connect to blockchain node")
        
        self.contract_address = '0xf47038eB22fD7113DAdeCD0423b45A67830f60e4'
        self.contract_abi = json.loads("""[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "txId",
				"type": "string"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "FundRecorded",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "txId",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "purpose",
				"type": "string"
			}
		],
		"name": "recordTransaction",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "transactions",
		"outputs": [
			{
				"internalType": "string",
				"name": "txId",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "purpose",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "transactionsCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]""")
        
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        # Use the first account from Ganache as the default account for sending transactions
        self.default_account = self.w3.eth.accounts[0]

    def add_transaction(self, tx_data):
        # NOTE: The smart contract's recordTransaction function expects Ethereum addresses 
        # for sender and receiver. However, the application uses string names ("GovDept01", "Asha").
        # For this demonstration, we will use the default Ganache account for both the sender 
        # and receiver addresses on the blockchain transaction. A real-world application would 
        # need a system to map user names to their blockchain addresses.
        tx_hash = self.contract.functions.recordTransaction(
            tx_data['tx_id'],
            self.default_account, # Mock sender address from Ganache
            self.default_account, # Mock receiver address from Ganache
            int(tx_data['amount']),
            tx_data['purpose']
        ).transact({'from': self.default_account})
        
        # Wait for the transaction to be mined
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        # Return the block hash and number for confirmation
        return {
            "block_hash": receipt.blockHash.hex(),
            "block_number": receipt.blockNumber,
            "tx_hash": receipt.transactionHash.hex()
        }
