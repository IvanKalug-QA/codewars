# In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula
#
# (
# 𝑛
# 𝑘
# )
# =
# 𝑛
# !
# 𝑘
# !
# (
# 𝑛
# −
# 𝑘
# )
# !
# (
# k
# n
# ​
#  )=
# k!(n−k)!
# n!
# ​
#
# where n denotes a row of the triangle, and k is a position of a term in the row.
#
# Pascal's Triangle
#
# You can read Wikipedia article on Pascal's Triangle for more information.
#
# Task
# Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.
#
# Example:
# n = 1: [1]
# n = 2: [1,  1, 1]
# n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]

def pascals_triangle(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1, 1]
    result_pascals = [[1], [1, 1]]
    pascal_triangls = [1, 1, 1]
    for i in range(2, n):
        result = [1]
        for j in range(len(result_pascals[-1]) - 1):
            result.append(result_pascals[-1][j] + result_pascals[-1][j+1])
        result.append(1)
        result_pascals.append(result)
        for number in result:
            pascal_triangls.append(number)
    return pascal_triangls