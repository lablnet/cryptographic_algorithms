# Euclidean algorithm for gcd of two numbers, recursive.
def gcd_r(a: float, b: float):
    return a if b == 0 else gcd_r(b, a % b)


# Euclidean algorithm for gcd of two numbers, iterative.
def gcd_i(a: float, b: float):
    while b != 0:
        temp = b
        b = a % b
        a = temp
        # a, b = b, a % b
    return a


# Test cases for gcd_r and gcd_i.
if __name__ == "__main__":
    def test_gcd():
        assert gcd_r(973, 301) == 7
        assert gcd_i(973, 301) == 7
        assert gcd_r(973, -301) == -7
        assert gcd_i(973, -301) == -7
        assert gcd_r(19, 17) == 1
        assert gcd_i(19, 17) == 1
        assert gcd_r(10434, 524) == 2
        print("All tests passed successfully")

    test_gcd()
