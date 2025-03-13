# Task
# In this kata you will be given a list consisting of unique elements except for one thing that appears twice.
#
# Your task is to output a list of everything inbetween both occurrences of this element in the list.
#
# Examples:
# [0, 1, 2, 3, 4, 5, 6, 1, 7, 8] => [2, 3, 4, 5, 6]
# ['None', 'Hello', 'Example', 'hello', 'None', 'Extra'] => ['Hello', 'Example', 'hello']
# [0, 0] => []
# [True, False, True] => [False]
# ['e', 'x', 'a', 'm', 'p', 'l', 'e'] => ['x', 'a', 'm', 'p', 'l']
# Notes
# All elements will be the same datatype.
# All used elements will be hashable.

def duplicate_sandwich(arr):
    start = 0
    end = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                start = i
                end = j
    return arr[start + 1: end]