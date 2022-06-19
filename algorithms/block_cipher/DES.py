"""
    DES.py Data Encryption Standard implementation.
"""

# Initial permutation.
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final permutation.
IPI = [40, 8, 48, 16, 56, 24, 64, 32,
       39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30,
       37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28,
       35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26,
       33, 1, 41, 9, 49, 17, 57, 25]

# Plaintext permutation.
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# key permutation.
PCI1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# key permutation 2.
PCI2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# E-box permition.
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# S-box substitution.
S = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S1
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ],
]

"""
    * All of the above permutations tables are copied from book Understanding Cryptography by Christof Paar.
"""


# Function to convert string to 64 bits chunks.
def convert_str_to_64_bit_chunks(s: str) -> list:
    assert len(s) % 8 == 0, "String length must be multiple of 8."
    return [s[i:i+8] for i in range(0, len(s), 8)]


# Function to convert binary to hex.
def bin_to_hex(s: str) -> str:
    return ''.join([hex(int(s[i:i+4], 2))[2:] for i in range(0, len(s), 4)])


# Function to convert hex to binary.
def hex_to_bin(s: str) -> str:
    return ''.join([bin(int(s[i:i+2], 16))[2:].zfill(8) for i in range(0, len(s), 2)])


# Function to convert a string to a list of bits.
def str_to_binary(s: str):
    return ''.join(format(ord(x), 'b').zfill(8) for x in s)


# Function to convert a list of bits to a string.
def bin_to_str(binary: str) -> str:
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


# Function to generate a random key.
def generate_key():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))


# Function to perform permutations.
def ip_permutation(plaintext: str, permutation: list):
    LR = []
    for i in permutation:
        LR.append(int(plaintext[i - 1]))

    L = LR[:32]
    R = LR[32:]

    return L, R


# Function to perform P permutations.
def p_permutation(plaintext: list) -> list:
    L, R = ip_permutation(plaintext, P)
    return L + R


# Function to perform ip initial permutations.
def ip1_permutation(plaintext: str):
    return ip_permutation(plaintext, IP)


# Function to perform final permutations.
def ipi_permutation(plaintext: str):
    return ip_permutation(plaintext, IPI)


# Function to perform PCI permutations.
def pci_permutation(key: str):
    cd = []
    for i in PCI1:
        cd.append(int(key[i-1]))

    C = cd[:28]
    D = cd[28:]
    return C, D


# Function to perform PCI-2 permutations.
def pci2_permutation(C: list, D: list):
    cd = C + D
    newKey = []
    for i in PCI2:
        newKey.append(int(cd[i-1]))
    return newKey


# Function to generate keys.
def generate_keys(key: str) -> list:
    key = str_to_binary(key)
    C, D = pci_permutation(key)
    K = []
    # left rotate sechduled.
    for i in [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]:
        # Left rotate C and D.
        C = C[i:] + C[:i]
        D = D[i:] + D[:i]
        K.append(pci2_permutation(C, D))
    return K


# Function to generate keys in reverse order.
def generate_keys_reverse(key: str) -> list:
    key = str_to_binary(key)
    C, D = pci_permutation(key)
    K = []
    for i in [0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]:
        if i == 0:
            K.append(pci2_permutation(C, D))
            continue
        # Right rotate C and D.
        C = C[-i:] + C[:-i]
        D = D[-i:] + D[:-i]
        K.append(pci2_permutation(C, D))
    return K


# Function to perform E expend permutations. It provides difusion.
def r_expend_permutation(R: list) -> list:
    return [R[i - 1] for i in E]


# Function to perform XOR operation.
def x_or(a: list, b: list) -> list:
    return [int(x) ^ int(y) for x, y in zip(a, b)]


# Function to perform S-box permutations. It provides confusion.
def s_substitution(R: list):
    new_r = []
    for i in range(0, 8):
        row = R[i * 6: i * 6 + 5]
        col = row[1] * 8 + row[2] * 4 + row[3] * 2 + row[4]
        row = row[0] * 2 + row[-1]
        new_r.append(str_to_binary(str(S[i][row][col])))
    return "".join(new_r)


# Function to perform f function operations.
def f_function(R: list, K: list) -> list:
    new_r = r_expend_permutation(R)  # Expend 32 bits to 48 bits.
    r_xor = x_or(new_r, K)
    s = s_substitution(r_xor)
    p = p_permutation(s)
    return p


# Main function to perform DES encryption/Description.
def des(plaintext: str, K: list) -> str:
    L, R = ip1_permutation(plaintext)
    for i in range(16):
        old_r = R
        f_output = f_function(R, K[i])
        R = x_or(L, f_output)
        L = old_r
    # swapped L and R and perform final permutations.
    L, R = ipi_permutation(R + L)
    return ''.join(str(x) for x in L + R)


# Function to perform DES encryption.
def des_encrypt(plaintext: str, key: str) -> str:
    ciphers = ""
    for text in convert_str_to_64_bit_chunks(plaintext):
        ciphers += des(str_to_binary(text), generate_keys(key))
    return bin_to_hex(ciphers)


# Function to perform DES decryption.
def des_decrypt(ciphertext: str, key: str) -> str:
    plaintext = ""
    for cipher in convert_str_to_64_bit_chunks(bin_to_str(hex_to_bin(ciphertext))):
        plaintext += des(str_to_binary(cipher), generate_keys_reverse(key))
    return bin_to_str(plaintext)


if __name__ == "__main__":
    text = "A quick brown fox jumps over the lazy dog, and then he goes to sleep!!!!"
    key = "Cg%6xsvA"  # generate_key()
    cipher = des_encrypt(text, key)
    plaintext = des_decrypt(cipher, key)
    print("key", key)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
