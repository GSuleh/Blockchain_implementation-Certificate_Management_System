from Account import *
from DigitalSignature import *

class Operations:
    # Create operation
    def __init__(self, sender=Account(), recipient=Account(), amount=0, signature=b''):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
        
    def getSignature(self):
        private_key = open("private_key.pem", "rb")
        message = "test"
        dg = DigitalSignature()
        self.signature = dg.signData(str(message), private_key.read().decode(encoding="utf-8"))
        return self.signature
    
    def verifySignature(self, signature):
        public_key = open("public_key.pem", "rb")
        message = "test"
        digitalsignature = signature
        signature = DigitalSignature()
        sign = signature.verifySignature(message, digitalsignature, public_key.read().decode(encoding="utf-8"))

    def createOperation(self):
        self.getSignature()
        return self.sender.accountID, self.recipient.accountID, self.amount, self.signature
    
    def verifyOperation(self, signature):
        if self.amount < self.sender.balance:
            self.verifySignature(signature)
        else:
            print("Insufficient Balance")