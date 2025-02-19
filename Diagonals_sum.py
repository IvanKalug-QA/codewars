# Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)
#
# Matrix = array of n length whose elements are n length arrays of integers.
#
# 3x3 example:
#
# [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 7, 8, 9 ]
# ]
#
# returns --> 30 // 1 + 5 + 9 + 3 + 5 + 7

def sum_diagonals(matrix):
    if not matrix:
        return 0
    counter = 0
    i = 0
    j = 0
    while i < len(matrix) and j < len(matrix[0]):
        counter += matrix[i][j]
        i += 1
        j += 1
    i = 0
    j = len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        counter += matrix[i][j]
        i += 1
        j -= 1
    return counter