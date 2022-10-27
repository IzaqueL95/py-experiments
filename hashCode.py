import hashlib

class HashCode:
    principalHash = '12abcd'

    def __int__(self, hash):
        self.principalHash = hash

    def hashReturn(self,hash):
        return  hashlib.sha256(hash.encode('utf-8')).hexdigest()

comb = HashCode()

print(comb.hashReturn('abcd'))

