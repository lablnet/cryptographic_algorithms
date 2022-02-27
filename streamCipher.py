# Convert string text into bits, then into binary.
def bits(text):
    return "".join(["0" * (8 - len(bin(ord(char))[2:])) + bin(ord(char))[2:] for char in text])

# convert binary to string
def binary(b):
    return "".join([chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8)])

# Generate key from bits.      
def generateKey(size):
    import random
    return [random.randint(0, 1) for n in range(0, size)]   

# encrypt stream cipher.
def encrypt(bits, key):
    return "".join([str(int(bit) ^ int(k)) for bit, k in zip(bits, key)])

# Decrypt stream cipher [as we taking XOR, just call encrypt function again].
def decrypt(cipher, key):
    return encrypt(cipher, key)


text = "This is secret texts"
text_bits = bits(text)
key = generateKey(len(text_bits))
# print(text_bits)
# print(key)
cipher = encrypt(text_bits, key)
d = decrypt(cipher, key)
print(cipher)
print(binary(d))
