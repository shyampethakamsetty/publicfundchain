
# Blockchain Guide — Ganache, Solidity & web3.py Integration

## Overview
This guide helps you connect the backend to a local Ethereum testnet (Ganache) and store transactions on-chain via a simple Solidity contract.

## Prerequisites
- Install Ganache UI or `ganache-cli`
- Install `web3` / `web3.py` in backend environment

## Steps

### 1) Smart Contract (contracts/Fund.sol)
- Simple contract `FundLedger` with `recordTransaction(...)` event (scaffold included).
- Compile contract using `solc` or use Truffle/Hardhat for compilation & deployment (recommended: Hardhat for JS teams).

### 2) Run Ganache
- Start Ganache on port 8545.
- Note the RPC URL (e.g., `http://127.0.0.1:8545`) and accounts' private keys (for demo wallets).

### 3) Deploy Contract
- Use `web3.py` or `web3.js` to deploy contract from a demo account to Ganache.
- Store contract ABI and address in `backend/config.json` or environment variable.

### 4) Recording transactions
- In `backend/api/routes.py` when creating a transaction:
  1. Call contract method `recordTransaction(txId, senderAddr, receiverAddr, amount, purpose)`
  2. Wait for transaction receipt and capture on-chain `transactionHash`
  3. Write `transactionHash` into DB `transactions.hash` column

### 5) Block explorer UI
- The frontend can show blockchain explorer by reading blocks from Ganache via `web3.py`:
  - `web3.eth.get_block(block_number, full_transactions=True)`
  - Display `block.number`, `block.hash`, `transactions`

### 6) Security notes (for production)
- Do not store private keys in code; use secure vaults.
- For demo, use Ganache accounts but make clear in pitch that keys are demo-only.
