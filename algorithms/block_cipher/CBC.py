# Block Cipher Mode: CBC (Cipher Block Channing)
# In CBC same key is used for encryption of larger blocks of data but we add a random initialization vector to each block.
# Undeerstanding cryptography by christof Paar, Page: 143

from DES import (
    convert_str_to_64_bit_chunks,
    str_to_binary,
    bin_to_hex,
    bin_to_str,
    generate_keys,
    generate_keys_reverse,
    des,
    hex_to_bin,
    x_or
)


# IV is the initialization vector that add the randomness to the ciphertext.
IV = "11111111"


# Function to perform DES encryption in CBC mode.
def encrypt(plaintext: str, key: str) -> str:
    assert len(plaintext) % 8 == 0, "Plaintext must be a multiple of 8"

    # Convert the plaintext into 64-bit chunks
    x = convert_str_to_64_bit_chunks(plaintext)

    # DEF: Y1 = enc((x1 ⊕ IV), key)
    # Get first 64 bit block, then convert it to binary and xor with IV
    x1 = x_or(str_to_binary(x[0]), str_to_binary(IV))
    y = des(x1, generate_keys(key))
    ciphertext = y

    for i in range(1, len(x)):
        # DEF: Yi = enc((Xi ⊕ Yi), key)
        # Xor the current block with the previous ciphertext, then encrypt it
        Yi = x_or(y, str_to_binary(x[i]))
        Yi = des(Yi, generate_keys(key))
        y = Yi
        ciphertext += Yi

    return bin_to_hex(ciphertext)


# Function to perform DES decryption in CBC mode.
def decrypt(ciphertext: str, key: str) -> str:
    assert len(ciphertext) % 8 == 0, "Ciphertext must be a multiple of 8"

    # Convert the ciphertext into 64-bit chunks
    y = convert_str_to_64_bit_chunks(bin_to_str(hex_to_bin(ciphertext)))

    # get first 64 bit block, then convert it to binary and xor with IV
    x1 = des(str_to_binary(y[0]), generate_keys_reverse(key))
    x1 = x_or(x1, str_to_binary(IV))
    x1 = "".join(str(i) for i in x1)
    plaintext = x1

    for i in range(1, len(y)):
        Xi = des(str_to_binary(y[i]), generate_keys_reverse(key))
        Xi = x_or(Xi, str_to_binary(y[i - 1]))
        x1 = "".join(str(i) for i in Xi)
        plaintext += x1

    return bin_to_str(plaintext)


if __name__ == "__main__":
    text = "Hello, World! this is the secet message sending over the network"
    key = "Cg%6xsvA"  # generate_key()
    cipher = encrypt(text, key)
    plaintext = decrypt(cipher, key)
    print("keys:", key)
    print("Plaintext:", text)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
