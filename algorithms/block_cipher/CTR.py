# Counter Mode (CTR)
# This is a stream cipher, which use block cipher(AES, DES, DESX) as key stream generator.
# As a result of the use of an IV with counter, the CTR encryption is also nondeterministic
# The IV with counter enable uniqueness of the ciphertext.
# The CTR can be paralized.
# Undeerstanding cryptography by christof Paar, Page: 146

from DES import (
    convert_str_to_64_bit_chunks,
    str_to_binary,
    bin_to_hex,
    bin_to_str,
    generate_keys,
    des,
    hex_to_bin,
    x_or
)

# IV is the initialization vector, with the counter appended to the end.
IV = "0000"


# Function to encrypt in CTR mode.
def encrypt(text: str, key: str) -> str:
    assert len(text) % 8 == 0, "Text must be a multiple of 8"

    # Convert the text into 64-bit chunks
    v = convert_str_to_64_bit_chunks(text)

    output = ""
    for i in range(0, len(v)):
        # Generate counter
        zeros = "".join(str(i) for i in ["0" for i in range(4 - len(str(i)))])
        counter = str(zeros) + str(i)

        # DEF: Vi = enc (IV || counter) ⊕ Vi,
        # Encrypt the iv with the key and xor with the current block.
        Vi = x_or(des(str_to_binary(IV + str(counter)), generate_keys(key)),
                  str_to_binary(v[i]))
        v1 = "".join(str(i) for i in Vi)

        # Append the current ciphertext to the output.
        output += v1

    return bin_to_hex(output)


# Function to decrypt in CFB mode.
def decrypt(ciphertext: str, key: str) -> str:
    return bin_to_str(hex_to_bin(encrypt(bin_to_str(hex_to_bin(ciphertext)), key)))


if __name__ == "__main__":
    text = "Hello, World! this is the secet message sending over the network"
    key = "Cg%6xsvA"  # generate_key()
    cipher = encrypt(text, key)
    plaintext = decrypt(cipher, key)
    print("keys:", key)
    print("Plaintext:", text)
    print("Cipher:", cipher)
    print("Dec Plaintext:", plaintext)
