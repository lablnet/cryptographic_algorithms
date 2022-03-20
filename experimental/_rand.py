# Just for experiment.

# random function.
A = 1103515245
B = 2345
M = 2147483647

def _rand(seed: int) -> int:
    assert seed >= 4
    # generate list of size M.
    r = [0] * seed  
    r[0] = seed
    for i in range(1, seed - 2):
        r[i] = (A * r[i] + B) % M
    
    # convert to string
    r = "".join([str(i) for i in r])
    return r 

def rand(a, b, seed = 10):
    r = _rand(seed)
    return int(r[a:b])

print(rand(1, 25))    