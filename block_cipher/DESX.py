from DES import (
    x_or,
    convert_str_to_64_bit_chunks,
    str_to_binary,
    bin_to_hex,
    bin_to_str,
    generate_keys,
    generate_keys_reverse,
    des,
    hex_to_bin
)


# Function to perform DESX decryption.
def desx_encrypt(plaintext: str, key1: str, key2: str) -> str:
    ciphers = ""
    for text in convert_str_to_64_bit_chunks(plaintext):
        ciphers += "".join(str(i) for i in x_or(str_to_binary(key2),
                           des(str_to_binary(text), generate_keys(key1))))
    return bin_to_hex(ciphers)


# Function to perform DESX decryption.
def desx_decrypt(ciphertext: str, key1: str, key2: str) -> str:
    plaintext = ""
    for cipher in convert_str_to_64_bit_chunks(bin_to_str(hex_to_bin(ciphertext))):
        plaintext += des("".join(str(c) for c in x_or(str_to_binary(key2),
                         str_to_binary(cipher))), generate_keys_reverse(key1))
    return bin_to_str(plaintext)


if __name__ == "__main__":
    text = "A quick brown fox jumps over the lazy dog, and then he goes to sleep!!!!"
    key1 = "Cg%6xsvA"  # generate_key()
    key2 = "Ce%5xtyi"  # generate_key()
    cipher = desx_encrypt(text, key1, key2)
    plaintext = desx_decrypt(cipher, key1, key2)
    print("keys:", key1, key2)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
