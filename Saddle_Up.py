# Task
# Find all the saddle points of a non-empty matrix of integers. A saddle point is an element that is minimal in its row and maximal in its column. Return them in a list of (row,column) coordinates. The order of the saddle points in the list is irrevelant.

# Example
# Consider the following matrix:

# 6 4 3
# 7 0 2
# 4 3 2
# 5 3 3
# The row minimums are 3, 0, 2, 3 (at positions 1 and 2).
# The column maximums are 7, 4, 3 (at positions 0 and 3).
# Therefore the 3's in the 3rd column are saddle points, but the 3's in the 2nd column are not.
# Return [(0,2), (3,2)]] or [(3,2), (0,2)].
# Constraints
# Number of rows r and number of columns c satisfy1 ≤ r,c ≤ 500. So you should think about efficiency (a little).

# Note
# Matrix saddle points are used in game theory to identify optimal strategies in two-person zero-sum games - see here. There is a related saddle point concept for functions, which has even wider applications - see here.

def find_saddle_points(matrix):
    if not matrix or not matrix[0]:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    row_mins = set()
    for i in range(rows):
        min_val = min(matrix[i])
        for j in range(cols):
            if matrix[i][j] == min_val:
                row_mins.add((i, j))
    col_maxs = set()
    for j in range(cols):
        max_val = max(matrix[i][j] for i in range(rows))
        for i in range(rows):
            if matrix[i][j] == max_val:
                col_maxs.add((i, j))
    return list(row_mins & col_maxs)