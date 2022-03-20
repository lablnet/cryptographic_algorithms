# Create a-z list.
alphabet = []
for i in range(97, 123):
    alphabet.append(chr(i))

def encrypt(plaintext, key = 3, encrypt = True):
    plaintext = plaintext.lower()
    cipher = ""
    for char in plaintext:
        if char not in alphabet:
            cipher += char
            continue

        if encrypt == True:
            cipher += alphabet[(alphabet.index(char) + key) % 26]
        else:
            cipher += alphabet[(alphabet.index(char) - key) % 26]

    return cipher

def decrypt(ciphertext, key = 3):
    return encrypt(ciphertext, key, False)


def attack(cipher):
    for k in range(26):
        print(k, decrypt(cipher, k))

text = "Hello World!, this is Umer"
cipher = encrypt(text)

print(cipher)
print()
print(decrypt(cipher))
print()
attack(cipher)
