from ecdsa import SigningKey, VerifyingKey, NIST192p
from hashlib import sha256
# NIST192p private key length is 24 bytes

class DigitalSignature:
    msg: str
    public_key: str
    private_key: str
    signature_hex_string: str
        
                             
    #returns it as str hex digitalsignature.
    def signData(self, msg, private_key):
        
        msgHash = sha256(msg.encode('utf-8')).digest()
        sk = SigningKey.from_string(bytearray.fromhex(private_key))
        signature = sk.sign(msgHash)
        self.signature_hex_string = str(signature.hex())
        
        file_out = open("digitalsignature.pem", "wb")
        file_out.write(self.signature_hex_string.encode('utf-8'))
        file_out.close()
        
        return self.signature_hex_string
        
    #returns whether the signature is valid or not.
    def verifySignature(self, msg, signature, public_key):
        msgHash = sha256(msg.encode('utf-8')).digest()
        vk = VerifyingKey.from_string(bytearray.fromhex(public_key))
        signature = bytearray.fromhex(signature)
        print('Verify transmited data', vk.verify(signature, msgHash))



