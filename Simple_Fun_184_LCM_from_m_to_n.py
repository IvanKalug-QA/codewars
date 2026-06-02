# Task
# Your task is to find the smallest number which is evenly divided by all numbers between m and n (both inclusive).

# Example
# For m = 1, n = 2, the output should be 2.

# For m = 2, n = 3, the output should be 6.

# For m = 3, n = 2, the output should be 6 too.

# For m = 1, n = 10, the output should be 2520.

# Input/Output
# [input] integer m
# 1 ≤ m ≤ 25

# [input] integer n
# 1 ≤ n ≤ 25

# [output] an integer


import math

def mn_lcm(m, n):
    start = min(m, n)
    end = max(m, n)
    result = 1
    for i in range(start, end + 1):
        result = result * i // math.gcd(result, i)
    return result