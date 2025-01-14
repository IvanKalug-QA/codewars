# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:
#
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(s):
    up = 0
    down = len(s[0]) - 1
    right = 0
    left = len(s) - 1
    result = []
    while right <= left:
        for i in range(up, down + 1):
            result.append(s[right][i])
        for i in range(right + 1, left+1):
            result.append(s[i][down])
        for i in range(down - 1, up - 1, -1):
            result.append(s[left][i])
        for i in range(left - 1, right, -1):
            result.append(s[i][up])
        right += 1
        left -= 1
        up += 1
        down -= 1
    return result