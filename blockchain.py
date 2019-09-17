# https://github.com/harsathAI/Simple-BlockChain-With-NONCE/blob/master/Blockchain.py

import hashlib
import json
from datetime import date
from pprint import pprint

def printObj(obj):
    return json.dumps(obj, default=lambda obj: vars(obj), indent=1)

class Block:
    def __init__(self, timestamp, transactions, previousHash):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        hash = hashlib.sha256()

        hash.update(
            str(self.previousHash).encode("utf-8") +
            str(self.timestamp).encode("utf-8") + 
            json.dumps(self.transactions, separators=(',', ':')).encode("utf-8") +
            str(self.nonce).encode("utf-8")
        )
        return hash.hexdigest()

    def mineBlock(self, difficulty):
        
        zeros = []
        for _ in range(difficulty + 1):
            zeros.append("")

        while self.hash[0:difficulty] != "0".join(zeros):
            self.nonce += 1
            self.hash = self.calculateHash()
        
        print("Block Mined : " + self.hash)
    
    # To complete
    """ 
    def hasValidTransactions(self):
        for tx in self.transactions:
            if tx.isValid();
            return False
        return True
    """

class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 4
        self.pendingTransactions = []
        self.miningReward = 1000

    def createGenesisBlock(self):
        today = date.today().strftime("%d/%m/%Y")
        return Block(today, "Genesis Block", "0")

    def getLatestBlock(self):
        return printObj(self.chain[len(self.chain) - 1])

    def getPendingTransactions(self):
        return printBlock(self.pendingTransactions)

    def minePendingTransactions(self, miningRewardAddress):
        today = date.today().strftime("%d/%m/%Y")
        block = Block(today, self.pendingTransactions, self.getLatestBlock().__hash__)
        block.mineBlock(self.difficulty)

        print("Block Mined !")

        self.chain.append(block)

        self.pendingTransactions = [
            # To complete 
        ]
    
    def addTransaction(transaction):
        print("à faire :D")

    def getBalanceOfAdress(self, adress):
        balance = 0

        for block in self.chain:
            for trans in block.transactions:
                if trans.fromAdress == adress:
                    balance -= trans.amount
                
                if trans.toAdress == adress:
                    balance += trans.amount

        return balance
    
    def isChainValid(self):
        i = 1
        for _ in len(self.chain):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]

            if currentBlock.hasValidTransactions():
                return False
            
            if currentBlock.hash != currentBlock.calculateHash():
                return False

            if currentBlock.previousHash !== previousBlock.hash:
                return False
        
        return True
    
class Transaction:
    def __init__(self, fromAdress, toAdress, amount):
        self.fromAdress = fromAdress
        self.toAdress = toAdress
        self.amount = amount
    
    def calculateHash(self){

        hash = hashlib.sha256()

        hash.update(  # To update
            str(self.fromAdress).encode("utf-8") +
            str(self.toAd).encode("utf-8") + 
            json.dumps(self.transactions, separators=(',', ':')).encode("utf-8") +
            str(self.nonce).encode("utf-8")
        )
        return hash.hexdigest()
    }

    # Add others functions

test = BlockChain()
test.minePendingTransactions("mwa")

