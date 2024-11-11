# You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.
#
# Examples
# []                   -->  0
# [1, 2, 3]            -->  3
# ["x", "y", ["z"]]    -->  4
# [1, 2, [3, 4, [5]]]  -->  7
# The input will always be an array.

def rec(a):
    res = 0
    for i in a:
        if not isinstance(i, list):
            res += 1
        else:
            res += 1 + rec(i)
    return res


def deep_count(a):
    return rec(a)