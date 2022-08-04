import collections
from hashlib import sha256

class Transaction:

    def __init__(self, transaction=[], nonce=0):
        self.transaction = transaction
        self.nonce = nonce

    def createOperation(self, transaction, nonce):
        t = self.transaction, self.nonce
        return collections.OrderedDict({
            'transactionId': sha256(str(t).encode('utf-8')).digest().hex(),
            'Tansactions': transaction,
            'nonce': nonce})
