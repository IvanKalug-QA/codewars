# Task:
# Given a two dimensional array, return the co-ordinates of x.
#
# If x is not inside the array, or if x appears multiple times, return [].
#
# The co-ordinates should be zero indexed in row-major order.
# You should assume you will always get an array as input. The array will only contain 'x's and 'o's.
#
# Examples
# Input: []
# Return an empty array if input is an empty array => []
#
# Input: [
#   ['o', 'o'],
#   ['o', 'o']
# ]
# Return an empty array if no x found => []
#
# Input: [
#   ['x', 'o'],
#   ['o', 'x']
# ]
# Return an empty array if more than one x found => []
#
# Input: [
#   ['x', 'o'],
#   ['o', 'o']
# ]
# Return [0,0] when x at top left => [0, 0]
#
# Input: [
#   ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#   ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#   ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#   ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
#   ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o'],
#   ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
# ]
# Return [4,6] for the example above => [4, 6]

def x_marks_the_spot(mat):
    d = {}
    counter_x = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'x' and mat[i][j] not in d:
                d['x'] = [i, j]
                counter_x += 1
            elif mat[i][j] == 'x' and mat[i][j] in d:
                counter_x += 1
    return [] if 'x' not in d or counter_x > 1 else d['x']