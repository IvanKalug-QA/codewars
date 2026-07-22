# Get the next prime number!

# You will get a numbern (>= 0) and your task is to find the next prime number.

# Make sure to optimize your code: there will numbers tested up to about 10^12.

# Examples
# 5   =>  7
# 12  =>  13

def next_prime(n):
    if n < 2:
        return 2
    
    candidate = n + 1
    if candidate % 2 == 0:
        candidate += 1
    
    while True:
        if is_prime_miller_rabin(candidate):
            return candidate
        candidate += 2

def is_prime_miller_rabin(n):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    
    for a in [2, 3, 5, 7, 11, 13, 17]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True