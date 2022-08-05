from gcd import euclidean_i

# Function to find Euler's PHI function for a given number.
def euler_phi(m: int) -> int:
    rP = 0 # relative prime
    for i in range(1, m + 1):
        # If i is a relative prime to m, then add 1 to rP.
        if euclidean_i(i, m) == 1:
            rP += 1
    return rP

# Function to find Euler's PHI function for a given number optimically.
def euler_phi_totient(m: int) -> int:
    # Initial values.
    result = m
    p = 2
    
    # Loop until p is greater than m.
    while p * p <= m:
        # If p is a relative prime to m, then subtract result / p from result.
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        # Increment p.
        p += 1
    if m > 1:
        # If m > 1, then subtract result / m from result.
        result -= result // m       
    return result
            

if __name__ == "__main__":
    def test():
        assert euler_phi(1) == 1
        assert euler_phi(6) == 2
        assert euler_phi(12) == 4
        assert euler_phi(240) == 64
        assert euler_phi_totient(1) == 1
        assert euler_phi_totient(6) == 2
        assert euler_phi_totient(12) == 4
        assert euler_phi_totient(240) == 64
        assert euler_phi_totient(240403242234) == 80134414076
        print("All tests passed successfully")
    test()
