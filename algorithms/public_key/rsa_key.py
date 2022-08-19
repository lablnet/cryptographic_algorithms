from prime import getPrime
from algorithms.math.gcd import extended_euclidean_i, euclidean_i


def rsa_key_generator(bits: int, CRT: bool = False) -> dict:
    """
    Generate a public/private key pair using 2 * `bits`-bit keys.
    :param bits: key length in bits
    :param CRT: if True, use Chinese Remainder Theorem to generate the private key
    :return: {'public': (e, n), 'private': (d, n)}
    :type bits: int
    :rtype: dict
    :author: Muhammad Umer Farooq
    """
    import random
    # Step 1. Generate two large primes, p and q.
    p: int = getPrime(bits)
    q: int = getPrime(bits)
    # Step 2. Compute n by the equation n = p * q.
    n: int = p * q
    # Step 3. Compute phi(n) = (p - 1) * (q - 1).
    phi: int = (p - 1) * (q - 1)
    # Step 4. Choose an integer e s.t. 1 < e < phi(n) and gcd(e, phi(n)) = 1.
    e: int = random.randint(2, phi - 1)
    while euclidean_i(e, phi) != 1:
        # e and phi are not coprime, try again.
        e = random.randint(2, phi - 1)
    # Step 5. Compute d as d ≡ e^(-1) (mod phi(n)).
    d = extended_euclidean_i(e, phi)[1]
    
    if CRT:
        # Step 6 and 7. Compute  Dp and Dq as Dp ≡ dp (mod p - 1) and Dq ≡ dq (mod q - 1).
        Dp = d % (p - 1)
        Dq = d % (q - 1)
        # Step 8. Compute qInv.
        qInv = extended_euclidean_i(q, p)[1]
        
    # We done, the public key is (e, n) and the private key is (d, n).
    return {
        "public_key": (e, n),
        "private_key": (d, n) if not CRT else (Dp, Dq, qInv, n, p , q)
    }
