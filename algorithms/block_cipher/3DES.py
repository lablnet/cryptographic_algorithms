from DES import (
    str_to_binary,
    bin_to_hex,
    bin_to_str,
    generate_keys,
    generate_keys_reverse,
    hex_to_bin,
    des
)


# Function to perform 3DES encryption.
def triple_des_encrypt(plaintext: str, key1: str, key2: str, key3: str) -> str:
    cipher = des(des(des(str_to_binary(plaintext), generate_keys(key1)),
                     generate_keys_reverse(key2)), generate_keys(key3))
    return bin_to_hex(cipher)


# Function to perform 3DES decryption.
def triple_des_decrypt(ciphertext: str, key1: str, key2: str, key3: str) -> str:
    plaintext = des(des(des(hex_to_bin(ciphertext), generate_keys_reverse(key3)),
                        generate_keys(key2)), generate_keys_reverse(key1))
    return bin_to_str(plaintext)


if __name__ == "__main__":
    text = "Hi, Umer"
    key1 = "Cg%6xsvA"  # generate_key()
    key2 = "Ad%7fsfq"  # generate_key()
    key3 = "Lw%2x3uk"  # generate_key()
    cipher = triple_des_encrypt(text, key1, key2, key3)
    plaintext = triple_des_decrypt(cipher, key1, key2, key3)
    print("keys:", key1, key2, key3)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
