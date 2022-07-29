# Block Cipher Mode: ECB (Electronic Codebook)
# In ECB same key is used for encryption of larger blocks of data.

from DES import (
    convert_str_to_64_bit_chunks,
    str_to_binary,
    bin_to_hex,
    bin_to_str,
    generate_keys,
    generate_keys_reverse,
    des,
    hex_to_bin
)

# Function to perform DES encryption.


def encrypt(plaintext: str, key: str) -> str:
    ciphers = ""
    for text in convert_str_to_64_bit_chunks(plaintext):
        ciphers += des(str_to_binary(text), generate_keys(key))
    return bin_to_hex(ciphers)


# Function to perform DES decryption.
def decrypt(ciphertext: str, key: str) -> str:
    plaintext = ""
    for cipher in convert_str_to_64_bit_chunks(bin_to_str(hex_to_bin(ciphertext))):
        plaintext += des(str_to_binary(cipher), generate_keys_reverse(key))
    return bin_to_str(plaintext)


if __name__ == "__main__":
    text = "Hi, A quick brown fox jumps over the lazy dog, and then he goes to sleep"
    key = "Cg%6xsvA"  # generate_key()
    cipher = encrypt(text, key)
    plaintext = decrypt(cipher, key)
    print("keys:", key)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
