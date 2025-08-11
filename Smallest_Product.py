# Given a non-empty array of non-empty integer arrays, multiply the contents of each nested array and return the smallest total.
#
# Example
# input = [
#   [1, 5],
#   [2],
#   [-1, -3]
# ]
#
# result = 2

def smallest_product(a):
    res = []
    for i in a:
        prod = 1
        for j in i:
            prod *= j
        res.append(prod)
    return min(res)