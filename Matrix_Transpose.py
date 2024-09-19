# Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of the original are swapped.
#
# For example, the transpose of:
#
# | 1 2 3 |
# | 4 5 6 |
# is
#
# | 1 4 |
# | 2 5 |
# | 3 6 |
# The input to your function will be an array of matrix rows. You can assume that each row has the same length, and that the height and width of the matrix are both positive.

def transpose(matrix):
    l = list()
    le = 0
    while le < len(matrix[-1]):
        new = list()
        for i in range(len(matrix)):
            new.append(matrix[i][le])
        l.append(new)
        le += 1
    return l