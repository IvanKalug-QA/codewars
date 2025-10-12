# Task
# Given an array of up to 100 numbers ranging from 1 to 1000, determine how many distinct even sums can be obtained by combinations of 2 different elements ( i.e. different indices, not necessarily different numbers ).
#
# Assume you will always have at least 2 numbers.
#
# Example
# array: [5, 6, 7, 8, 9]
#
# combinations of 2 numbers:
#     [5, 6], [5, 7], [5, 8], [5, 9], [6, 7], [6, 8], [6, 9], [7, 8], [7, 9], [8, 9]
# sum:  11      12      13      14      13      14      15      15      16      17
#
# list of distinct even sums:    12, 14, 16
# number of distinct even sums:  3

def even_twins(numbers):
    result = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result.add(numbers[i] + numbers[j])
    return sum(1 if i % 2 == 0 else 0 for i in result)