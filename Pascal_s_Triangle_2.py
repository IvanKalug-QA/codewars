# Here you will create the classic Pascal's triangle.
# Your function will be passed the depth of the triangle and your code has to return the corresponding Pascal's triangle up to that depth.
#
# The triangle should be returned as a nested array. For example:
#
# pascal(5) -> [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
# To build the triangle, start with a single 1 at the top, for each number in the next row you just take the two numbers above it and add them together, except for the edges, which are all 1. e.g.:
#
#       1
#     1   1
#   1   2   1
# 1   3   3   1

def pascal(p):
    if p == 1:
        return [[1]]
    elif p == 2:
        return [[1], [1,1]]
    result = [[1], [1, 1]]
    while len(result) < p:
        arr = [1]
        for i in range(len(result[-1])-1):
            arr.append(result[-1][i] + result[-1][i+1])
        arr.append(1)
        result.append(arr)
    return result