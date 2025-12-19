# Given a positive integer N, return the largest integer k such that 3^k < N.

# For example,

# 3 --> 0
# 4 --> 1
# You may assume that the input to your function is always a positive integer.

import math
def largest_power(N):
    if N <= 1:
        return -1
    k = int(math.log(N-1, 3))
    while 3**(k+1) < N:
        k += 1
    while 3**k >= N:
        k -= 1
    return k