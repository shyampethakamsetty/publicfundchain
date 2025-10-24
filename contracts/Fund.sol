
// Simple solidity contract placeholder for fund ledger (not audited)
pragma solidity ^0.8.0;

contract FundLedger {
    struct Transaction {
        string txId;
        address sender;
        address receiver;
        uint256 amount;
        string purpose;
        uint256 timestamp;
    }

    Transaction[] public transactions;

    event FundRecorded(string txId, address indexed sender, address indexed receiver, uint256 amount);

    function recordTransaction(string memory txId, address sender, address receiver, uint256 amount, string memory purpose) public {
        transactions.push(Transaction(txId, sender, receiver, amount, purpose, block.timestamp));
        emit FundRecorded(txId, sender, receiver, amount);
    }

    function transactionsCount() public view returns (uint256) {
        return transactions.length;
    }
}
