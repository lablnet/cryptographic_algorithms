"""
diffie_hellman.py Diffie-Hellman key exchange algorithm.
Diffie-Hellman key exchange algorithm is a method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as originally conceived by Ralph Merkle and named after Whitfield Diffie and Martin Hellman.
:author: Muhammad Umer Farooq
"""

from prime import getPrime
import random

# Choose large prime P.
p = getPrime(512)

# Choose alpha such that 1 < alpha < p-1.
# Alpha is a primitive root modulo p.
alpha = random.randint(2, p-1)

# Note: Both p and alpha are public.


def KeyA(p: int, alpha: int) -> tuple:
    """
    KeyA is the public key of 1st person i.e Alice.
    :param p: Prime number
    :param alpha: Primitive root modulo p
    :return: KeyA, a
    :author: Muhammad Umer Farooq
    """

    # choose a = kpr,A ∈ {2,..., p−2}
    a = random.randint(2, p-1)
    # compute A = kpub ≡ α^a mod p
    # A is the public key of ist person i.e Alice.
    return (pow(alpha, a, p), a)


def keyB(p: int, alpha: int) -> tuple:
    """
    KeyB is the public key of 2nd person i.e Bob.
    :param p: Prime number
    :param alpha: Primitive root modulo p
    :return: KeyB, b
    :author: Muhammad Umer Farooq
    """
    # choose b = kpr,B ∈ {2,..., p−2}
    b = random.randint(2, p-1)
    # compute B = kpub,B ≡ α^b mod p
    # B is the public key of 2nd person i.e Bob.
    return (pow(alpha, b, p), b)


def keySecret(p: int, key: int, secret: int) -> int:
    """
    keyASecret is the secret key of 1st person i.e Alice.
    :param p: Prime number
    :param keyB: Public key of 2nd person i.e Bob.
    :param a: Private key of 1st person i.e Alice.
    :return: keySecret
    :author: Muhammad Umer Farooq
    """
    # compute k = Key, Key^secret mod p
    # k is the secret key of person.
    return pow(key, secret, p)


# If Alice and Bob both know the public parameters p and α computed in the set-up phase, they can generate a joint secret key k.
alice = KeyA(p, alpha)
bob = keyB(p, alpha)

print("Public Key of Alice: ", alice[0])
print("Public Key of Bob: ", bob[0])

# Note that the secret a,b is never transmitted over the network and it should be kept secret and stored securely.

keyAlice = keySecret(p, bob[0], alice[1])
keyBob = keySecret(p, alice[0], bob[1])

print("Secret Key of Alice: ", keyAlice)
print("Secret Key of Bob: ", keyBob)

# Look, both Alice and Bob have the same secret key.
# This is the power of Diffie-Hellman key exchange algorithm.
if (keyAlice == keyBob):
    print("Secret key is same for both Alice and Bob.")
