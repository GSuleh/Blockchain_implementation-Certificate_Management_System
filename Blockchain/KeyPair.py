from ecdsa import SigningKey, VerifyingKey, NIST192p

# NIST192p private key length is 24 bytes
# Third party library https://pypi.org/project/ecdsa/


class KeyPair:
    private_key_sk: str
    public_key_vk: str

        
    def genKeyPair(self):
        
        #new random private key. Used for signing
        self.private_key_sk = SigningKey.generate(curve=NIST192p)
        file_out = open("private_key.pem", "wb")
        file_out.write(self.private_key_sk.to_string().hex().encode('utf-8'))
        file_out.close()

        #public key. Used for verification
        self.public_key_vk = self.private_key_sk.verifying_key.to_string().hex()
        file_out = open("public_key.pem", "wb")
        file_out.write(str(self.public_key_vk).encode('utf-8'))
        file_out.close()
        
        return self.private_key_sk.to_string().hex(), (self.public_key_vk)
    
    def printKeyPair(self):
        self.private_key = open("private_key.pem", "rb")
        self.public_key = open("public_key.pem", "rb")
        print(self.private_key.read())
        print(self.public_key.read())

