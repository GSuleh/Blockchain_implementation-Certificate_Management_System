pip install tineyec

from tinyec import registry
import secrets


class KeyPair:
    private_key: str
    public_key: str


    #cryptographic elliptic curve over finite field, along with its generator point G.
    def genKeyPair(self):
        
        def compress_point(point):
            return hex(point.x) + hex(point.y % 2)[2:]
        
        ecc_curve = registry.get_curve('secp256r1')
        
        #new random private key.
        self.private_key = secrets.randbelow(ecc_curve.field.n)
        file_out = open("private_key.pem", "wb")
        file_out.write(str(hex(self.private_key)).encode('utf-8'))
        file_out.close()

        #private key * generator point G = public key.
        self.public_key = self.private_key * ecc_curve.g
        file_out = open("public_key.pem", "wb")
        file_out.write(str(compress_point(self.public_key)).encode('utf-8'))
        file_out.close()
        
        return hex(self.private_key), compress_point(self.public_key)
    
    def printKeyPair(self):
        self.private_key = open("private_key.pem", "rb")
        self.public_key = open("public_key.pem", "rb")
        print(self.private_key.read())
        print(self.public_key.read())
