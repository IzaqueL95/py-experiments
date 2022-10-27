import hashlib

password = 'ab123555'

hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

compare = 'ab1235555'

if(hashlib.sha256(compare.encode('utf-8')).hexdigest() == hash):
    print('math')
else:
    print('incorrect hash value')

