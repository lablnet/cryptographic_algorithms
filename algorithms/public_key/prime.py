import random
import string


def size(N) -> int:
    """size(N:long) : int
    Returns the size of the number N in bits.
    :source https://github.com/pycrypto/pycrypto/blob/65b43bd4ffe2a48bdedae986b1a291f5a2cc7df7/lib/Crypto/Util/number.py#L75
    """
    bits = 0
    while N >> bits:
        bits += 1
    return bits


def getRandomNBitInteger(n) -> int:
    """getRandomInteger(N:int):int
    This function copied, but modified as needed
    Return a random number with exactly N-bits, i.e. a random number
    between 2**(N-1) and (2**N)-1.
    :source https://github.com/pycrypto/pycrypto/blob/65b43bd4ffe2a48bdedae986b1a291f5a2cc7df7/lib/Crypto/Util/number.py#L91
    """
    seed = random.getrandbits(n >> 3)
    odd_bits = n % 8  # 0 <= odd_bits < 8
    if odd_bits != 0:  # if n is not a multiple of 8
        char = ord(random.choice(string.ascii_letters))  # random char
        seed = (seed << odd_bits) | (
            char & ((1 << odd_bits) - 1))  # mask out the high bits
    seed |= 2 ** (n-1)  # Ensure high bit is set
    assert size(seed) >= n  # make sure we have enough bits
    return seed


def robin_miller_test(p: int, k: int = 10) -> bool:
    """
    Function to perform the Miller-Rabin primality test to check if a number is prime.
    :param p: the number to test
    :param k: the number of testing rounds
    :return: True if p is probably prime, False if p is composite
    :type p: int
    :type k: int
    :rtype: bool
    :author: Muhammad Umer Farooq
    """
    # Base case, 2 is always prime.
    if p == 2:
        return True
    # None of others even are prime.
    if p % 2 == 0:
        return False
    # write n as 2 ^ s * d; where d is odd.
    s = 0
    d = p - 1
    while d % 2 == 0:  # d is odd.
        d = d // 2
        s += 1

    # Now, k tests.
    for i in range(k):
        # Choose a random witness for compositeness.
        a = random.randint(2, p - 2)
        x = pow(a, d, p)

        # If x = 1 or x = p - 1, then continue to next iteration.
        if x != 1 and x != p - 1:
            # check whether any other x is a factor of n
            for _ in range(1, s):
                x = pow(x, 2, p)
                if x == 1:
                    return False
                elif x == p - 1:
                    break
            # p is not prime.
            return False
    # p is prime.
    return True


def getPrime(N: int):
    """getPrime(N:int)
    Function to generate a random prime number of n bits.
    :source https://github.com/pycrypto/pycrypto/blob/65b43bd4ffe2a48bdedae986b1a291f5a2cc7df7/lib/Crypto/Util/number.py#L455
    """
    # Get the big integer and make sure it's odd.
    prime = getRandomNBitInteger(N) | 1
    while not robin_miller_test(prime):
        prime += 2
    return prime
