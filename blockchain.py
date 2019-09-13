# https://github.com/harsathAI/Simple-BlockChain-With-NONCE/blob/master/Blockchain.py

import hashlib
import json

class Block:
    def __init__(self, timestamp, transactions, previousHash):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.nonce = "0"

    def calculateHash(self):
        hash = hashlib.sha256()

        hash.update(
            str(self.previousHash).encode("utf-8") +
            str(self.timestamp).encode("utf-8") + 
            json.dumps(self.transactions, separators=(',', ':')).encode("utf-8") +
            str(self.nonce).encode("utf-8")
        )
        return hash.hexdigest()


test = Block("now", ["sddzs", "dzdzd"], "tggg")

print(test.calculateHash())
