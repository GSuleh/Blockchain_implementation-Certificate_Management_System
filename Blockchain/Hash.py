import hashlib

class Hash:

        
    def toSHA1(self, plain_text):
        
        hash = hashlib.sha1()
        hash.update(plain_text.encode('utf-8'))
        
        
        return hash.hexdigest()