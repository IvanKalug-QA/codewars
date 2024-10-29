# Task
# Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.
#
# Example
# For n = 152, the output should be 52;
#
# For n = 1001, the output should be 101.
#
# Input/Output
# [input] integer n
#
# Constraints: 10 ≤ n ≤ 1000000.
#
# [output] an integer

def delete_digit(n):
    result = [i for i in str(n)]
    len_n = len(result)
    max_digit = 0
    for i in range(len_n):
        temp = result[::]
        temp[i] = ''
        max_digit = max(max_digit, int(''.join(temp)))
    return max_digit