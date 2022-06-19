# find extended euclidean algorithm (Created by GitHub Coplit)
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcd(b % a, a)
        return g, x - (b // a) * y, y

# find modular inverse
def modinv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m
    
# Create a-z list.
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

def encrypt(plaintext, a = 3, b = 5, encrypt = True):
    cipher = ""
    for char in plaintext:
        if char not in alphabet:
            cipher += char
            continue
        if encrypt == True:
            cipher += alphabet[(a * alphabet.index(char) + b) % 26]
        else:
            cipher += alphabet[(modinv(a, 26) * (alphabet.index(char) - b)) % 26]

    return cipher

def decrypt(ciphertext, a = 3, b = 5):
    return encrypt(ciphertext, a, b, False)

def attack(cipher):
    for a in range(26):
        for b in range(26):
            print(a, b, decrypt(cipher, a, b))
            # if decrypt(cipher, a, b) == "Hello World!, this is Umer":
            #     print(a, b, decrypt(cipher, a, b))


text = "Hello World!, this is Umer"
cipher = encrypt(text)

print(cipher)
print()
print(decrypt(cipher))
#attack(cipher)
