from Hash import *

class Block():

    # Create Block
    def __init__(self, previous_hash, blockno, transactions):
        self.setOfTransactions = transactions
        self.prevHash = previous_hash
        self.nonce = ""
        self.time = str(datetime.datetime.now())
        self.blockID
        self.blockNO = blockno

    def blockID(self):
        if self.blockNO == 0 or  self.blockNO == None:
            return "Genesis"
        else:
            concat = self.prevHash, self.setOfTransactions, self.nonce, self.time
            return Hash().toSHA1(str(concat))

    def __str__(self):
        return ("Block#: %s Hash: %s Previous Hash: %s Transactions: %s Nonce: %s\ Time: %s\ " % (
            self.blockNO, self.blockID(), self.prevHash, self.setOfTransactions, self.nonce, self.time))