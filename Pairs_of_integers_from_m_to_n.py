# Implement a function that receives two integers m and n and generates a sorted list of pairs (a, b) such that m <= a <= b <= n.
#
# The input m will always be smaller than or equal to n (e.g., m <= n)
#
# Example
# m = 2
# n = 4
#
# result = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

def generate_pairs(m, n):
    result = []
    for i in range(m, n + 1):
        for j in range(i, n + 1):
            result.append((i, j))
    return result