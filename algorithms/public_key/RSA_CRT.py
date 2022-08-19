"""
RSA_CRT.py RSA with CRT optimization.
The RSA algorithm is an asymmetric cryptographic algorithm.
In RSA the data is encrypted using the public key and decrypted using the private key.
It is a public key encryption algorithm [public-key cryptography].
# 7.5.2 Fast Decryption with the Chinese Remainder Theorem Pg: 197. (Understanding Cryptography by Christo paar)
# Implementation of RSA and RSA-CRT Algorithms for Comparison of Encryption and Decryption Time in Androidbased Instant Message Applications (ISSN 2714-9714)
:author: Muhammad Umer Farooq
"""
import sys
sys.path.append('./')
from algorithms.utils import str_to_int, int_to_str
from rsa_key import rsa_key_generator
# The RSA-CRT public key is the same as the RSA system, namely (e , n) so the encryption algorithm does not change.
from RSA import encrypt


def decrypt(ciphertext: str, private_key: tuple):
    """
    Decrypt a string using the private key.
    :param ciphertext: the string to decrypt
    :param private_key: the private key
    :return: the decrypted string
    :type ciphertext: str
    :type private_key: tuple
    :rtype: str
    :author: Muhammad Umer Farooq
    """
    Dp, Dq, qInv, n, p, q = private_key
    m1 = pow(ciphertext, Dp, p)
    m2 = pow(ciphertext, Dq, q)
    h = (qInv * (m1 - m2)) % n
    plaintext = m2 + h * p
    return int_to_str(plaintext)


if __name__ == "__main__":
    # The bits size can be changed to 1024, 2048, 4096, etc.
    bits = 1024

    # generate key
    print("Generating key...")
    key = rsa_key_generator(bits, True)
    print("key", key)
    bob_public_key = key["public_key"]
    bob_private_key = key["private_key"]
    text = "Hello World"
    print("Alice wants to send a message to Bob")
    print("Alice encrypts the message with Bob's public key")
    alice_msg = encrypt(text, bob_public_key)
    print("Alice sends the message to Bob")
    print("Bob decrypts the message with his private key")
    plaintext = decrypt(alice_msg, bob_private_key)
    print("text", text)
    print("cipher", alice_msg)
    print("plaintext", plaintext)
