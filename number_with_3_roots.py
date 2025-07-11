# In mathematics, an nth root of a number x, where n is usually assumed to be a positive integer, is a number r which, when raised to the power n, yields x:
#
# r^n=x,
# Given number n, such that n > 1, find if its 2nd root, 4th root and 8th root are all integers (fractional part is 0), return true if it exists, false if not.
#
# # 2nd root of 256 is 16
# # 4th root of 256 is 4
# # 8th root of 256 is 2
# perfect_roots(256) # returns True

import math

def find_exponent(x, k):
    if x < 0:
        return False
    low = 1
    high = x
    while low <= high:
        mid = (low + high) // 2
        power = mid ** k
        if power == x:
            return True
        elif power < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def perfect_roots(n):
    return find_exponent(n, 2) and find_exponent(n, 4) and find_exponent(n, 8)