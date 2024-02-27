# Task
# Given a positive integer n, calculate the following sum:
#
# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.
#
# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47

def halving_sum(n):
    c = n
    f = 2
    for i in range(1, n + 1):
        c += n//f
        f *= 2
    return c