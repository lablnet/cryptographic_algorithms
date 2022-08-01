# Output Feedback Mode (OFB).
# This is a stream cipher, which use block cipher(AES, DES, DESX) as key generator.
# As a result of the use of an IV, the OFB encryption is also nondeterministic
# One advantage of the OFB mode is that the block cipher computations are independent of the plaintext.
# Hence, one can precompute one or several blocks si of key stream material.
# Undeerstanding cryptography by christof Paar, Page: 144

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

# IV is the initialization vector.
IV = "11111111"


# Function to encrypt in OFB mode.
def encrypt(text: str, key: str) -> str:
    assert len(text) % 8 == 0, "Text must be a multiple of 8"

    # Convert the text into 64-bit chunks
    v = convert_str_to_64_bit_chunks(text)

    # DEF: s1 = enc(IV) and v1 = s1 ⊕ v1
    # Encrypt IV and xor with the first block.
    s1 = des(str_to_binary(IV), generate_keys(key))
    v1 = x_or(s1, str_to_binary(v[0]))
    v1 = "".join(str(i) for i in v1)

    output = v1

    for i in range(1, len(v)):
        # DEF: Si = enc(Si-1) and Vi = Si ⊕ Vi-1
        # Encrypt the key stream with previous key stream and xor with the current block.
        Si = des(s1, generate_keys(key))
        Vi = x_or(Si, str_to_binary(v[i]))
        s1 = Si

        # Append the current ciphertext to the output.
        output += "".join(str(i) for i in Vi)

    return bin_to_hex(output)


# Function to decrypt in OFB mode.
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
