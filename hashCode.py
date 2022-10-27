import hashlib

class HashCode:
    principalHash = '12abcd'

    def __int__(self, hash):
        self.principalHash = hash

    def hashReturn(self,hash):
        return  hashlib.sha256(hash.encode('utf-8')).hexdigest()

comb = HashCode()

print(comb.hashReturn('abcd'))

print("**************************")
print("Qual o valor para o hash ?")
print("**************************")
verifyIFtrue = input("Por favor digite o valor... ")

if(hashlib.sha256(verifyIFtrue.encode('utf-8')).hexdigest() == comb.hashReturn('abcd')):
    print("hash encontrado..")
else:
    print("hash não corres
