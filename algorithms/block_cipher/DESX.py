from DES import (
    x_or,
    str_to_binary,
    bin_to_hex,
    bin_to_str,
    generate_keys,
    generate_keys_reverse,
    des,
    hex_to_bin
)


# Function to perform DESX encryption.
def desx_encrypt(plaintext: str, key1: str, key2: str) -> str:
    cipher = "".join(str(i) for i in x_or(str_to_binary(key2),
                                          des(str_to_binary(plaintext), generate_keys(key1))))
    return bin_to_hex(cipher)


# Function to perform DESX decryption.
def desx_decrypt(ciphertext: str, key1: str, key2: str) -> str:
    plaintext = des("".join(str(c) for c in x_or(str_to_binary(key2),
                                                 hex_to_bin(ciphertext))), generate_keys_reverse(key1))
    return bin_to_str(plaintext)


if __name__ == "__main__":
    text = "Hi, Umer"
    key1 = "Cg%6xsvA"  # generate_key()
    key2 = "Ce%5xtyi"  # generate_key()
    cipher = desx_encrypt(text, key1, key2)
    plaintext = desx_decrypt(cipher, key1, key2)
    print("keys:", key1, key2)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
