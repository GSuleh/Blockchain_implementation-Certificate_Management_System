# pip install pycoin

from pycoin.ecdsa.secp256k1 import secp256k1_generator
import hashlib, secrets

class digital_signature:
    msg: str
    public_key: str
    private_key: str
        
    #computes and returns a SHA3-256 hash
    def sha3_256Hash(msg):
        hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
        return int.from_bytes(hashBytes, byteorder="big")
    
    #takes a text message and 256-bit secp256k1 private key and calculates the ECDSA signature {r, s}
    #returns it as pair of 256-bit integers.
    def signData(self, msg, private_key):
        
        msgHash = sha3_256Hash(msg)
        signature = secp256k1_generator.sign(private_key, msgHash)
        return signature
    
    #takes a text message, a ECDSA signature {r, s} and a 2*256-bit ECDSA public key (uncompressed)
    #returns whether the signature is valid or not.
    def verifySignature(self, msg, signature, public_key):
        
        msgHash = sha3_256Hash(msg)
        valid = secp256k1_generator.verify(public_key, msgHash, signature)
        return valid 
