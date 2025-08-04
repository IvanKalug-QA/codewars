# Sexy primes are pairs of two primes that are 6 apart. In this kata, your job is to complete the function which returns true if x & y are sexy, false otherwise.
#
# Examples
# 5, 11   -->  true
# 61, 67  -->  true
# 7, 13   -->  true
# 5, 7    -->  false
# 1, 7    -->  false  (1 is not a prime)
# Note: x & y are always positive integers, but they are not always in order of precendence... For example you can be given either (5, 11) or (11, 5) - both are valid.

def is_prime(a):
    if a < 2:
        return False
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
def sexy_prime(x, y):
    return is_prime(x) and is_prime(y) and abs(x - y) == 6