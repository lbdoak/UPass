import secrets
import string
from hashlib import sha256
import os
from bloomfilter import BloomFilter
import pickle

def gen_password(len):
    try:
        len = int(len)
    except ValueError:
        raise ValueError("Password length must be an integer.")
    
    dict = string.ascii_letters + string.digits + string.punctuation
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    password += ''.join([secrets.choice(dict) for _ in range(len - 4)])

    secrets.SystemRandom().shuffle(password)
    password = ''.join(str(x) for x in password)

    return password

def gen_master(fp="../source/usr/!"):
    if os.path.exists(fp):
        with open(fp, 'rb') as fp:
            data = fp.read()
            bf = pickle.loads(data)
            return True, bf
    else:
        password = gen_password(16)
        secret = sha256(password.encode('utf-8')).hexdigest()
        bf = BloomFilter(1, 0.01)
        bf.put(secret)
        data = pickle.dumps(bf)
        with open(fp, 'wb') as fp:
            fp.write(data)

        return False, secret