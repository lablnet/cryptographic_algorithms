# Euclidean algorithm for gcd of two numbers, recursive.
def euclidean_r(a: float, b: float):
    return a if b == 0 else euclidean_r(b, a % b)


# Euclidean algorithm for gcd of two numbers, iterative.
def euclidean_i(a: float, b: float):
    while b != 0:
        temp = b
        b = a % b
        a = temp
        # a, b = b, a % b
    return a


# Extended Euclidean algorithm for gcd of two numbers, recursive.
def extended_euclidean_r(a: float, b: float):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_euclidean_r(b, a % b)
        return g, y, x - (a // b) * y


# Extended Euclidean algorithm for gcd of two numbers, iterative.
def extended_euclidean_i(a: float, b: float):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while b != 0:
        # Find Quotient and Remainder
        q = a // b
        r = a % b
        # Update values
        a, b = b, r
        # Linear combination
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return a, s0, t0


# Test cases for gcd_r and gcd_i.
if __name__ == "__main__":
    def test_gcd():
        assert euclidean_r(973, 301) == 7
        assert euclidean_i(973, 301) == 7
        assert euclidean_r(973, -301) == -7
        assert euclidean_i(973, -301) == -7
        assert euclidean_r(19, 17) == 1
        assert euclidean_i(19, 17) == 1
        assert euclidean_r(10434, 524) == 2
        assert extended_euclidean_i(973, 301) == (7, 13, -42)
        assert extended_euclidean_r(973, 301) == (7, 13, -42)
        print("All tests passed successfully")

    test_gcd()
