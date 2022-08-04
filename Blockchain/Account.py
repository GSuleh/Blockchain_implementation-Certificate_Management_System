from KeyPair import *
from DigitalSignature import *

class Account:
    def __init__(self):
        self.genAccount()

    def genAccount(self):
        key_pair = KeyPair()
        self.wallet = []
        self.balance = 0
        self.wallet.append(key_pair.genKeyPair())
        self.accountID = self.wallet[0][0]
        return self.wallet, self.accountID

    def addKeyPairToWallet(self):
        self.wallets.append(A.genKeyPair())

    def signData(self, msg, index):
        Sign = DigitalSignature()
        key = self.wallet[index][0]
        return Sign.signData(msg, key)

    def updateBalance(self, coins):
        self.balance = coins

    def getBalance(self):
        return self.balance

    def printBalance(self):
        print("Balance: ", self.balance)