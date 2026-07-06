# You are given two positive integer lists with a random number of elements (1 <= n <= 100). Create a GCD matrix and calculate the average of all values.

# Return a float value rounded to 3 decimal places.

# Example
# a = [1, 2, 3]
# b = [4, 5, 6]

# #       a =    1  2  3     b =
# gcd(a, b) = [ [1, 2, 1],   # 4
#               [1, 1, 1],   # 5
#               [1, 2, 3] ]  # 6

# average(gcd(a, b)) = 1.444

import math

def gcd_matrix(a, b):
    matrix = []
    total_sum = 0
    total_elements = len(a) * len(b)
    for i in range(len(b)):
        row = []
        for j in range(len(a)):
            gcd_value = math.gcd(a[j], b[i])
            row.append(gcd_value)
            total_sum += gcd_value
        matrix.append(row)
    average = total_sum / total_elements
    return round(average, 3)