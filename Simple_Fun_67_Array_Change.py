# Task
# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
#
# Example
# For arr = [1, 1, 1], the output should be 3.
#
# Input/Output
# [input] integer array arr
#
# Constraints:
#
# 3 ≤ inputArray.length ≤ 100,
#
# -10000 ≤ inputArray[i] ≤ 10000.
#
# [output] an integer
#
# The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
#
# It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type.

def array_change(arr):
    result = 0
    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:
            res = abs(arr[i-1] - arr[i]) + 1
            arr[i] += res
            result += res
    return result