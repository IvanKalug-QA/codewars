# Given an array of numbers, return an array, with each member of input array rounded to a nearest number, divisible by 5.

# For example, given the following array:

# [34.5, 56.2, 11, 13]
# should return

# [35, 55, 10, 15]
# Roundings have to be done like "in real life": 22.5 -> 25

import math
def round_to_five(arr):
    result = []
    for num in arr:
        rounded = math.floor((num + 2.5) / 5) * 5
        result.append(rounded)
    return result