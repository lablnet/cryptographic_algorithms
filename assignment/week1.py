import sys

MSGS ="" # ( ---  11 secret messages  --- )

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    import os
    return os.urandom(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print(c.encode('hex'))
    return c

def decrypt(key, cipher):
    text = strxor(key, cipher)
    print(text)

    return text


key = random(1024)
# ciphertexts = [encrypt(key, msg) for msg in MSGS]

# cipher text in hex encoded
cipher = "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83"
# decode that cipher hex coded to binary.
# decrypt(key, cipher.decode('hex'))
# convert binary to string.
key = key.decode('ascii', 'ignore')

print(key)