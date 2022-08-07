from Block import *
from Account import *

class Blockchain():
    difficulty = 1;
    # Genesis Block  and set its hash to "0"
    def __init__(self):
        self.blockHistory = []
        self.txDatabase = []
        self.coinDatabase = []
        self.faucet = 1000000
        

    def initBlockchain(self, block):
        self.blockHistory.append(block)

    def mineBlock(self, block):
        try:
            block.prevhash = self.blockHistory[-1].blockID()
        except IndexError:
            pass

        while True:
            if block.blockID()[:self.difficulty] == '0' * self.difficulty:
                self.initBlockchain(block)
                break
            else:
                block.nonce += 1

    def validateBlock(self):
        for i in range(2, len(self.blockHistory)):
            prev = self.blockHistory[i].prevhash
            current = self.blockHistory[i - 1].blockID()
            tx = self.blockHistory[i].transactions
            if prev != current or current[:self.difficulty] != '0' * self.difficulty and tx == tx:
                return False

        return True

    def getTokenFromFaucet(self, account, amount):
        self.faucet -= amount
        account.amount = amount
        return ("Account: %s Amount: %s" % (account.accountID, amount))
    
    def __str__(self):
        return ("Blockhistory: %s" % (self.blockHistory))