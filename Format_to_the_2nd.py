# Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the largest integer.
#
# For example, given 1, 23, 2, 17, 102, I wish to print out these numbers as follows:
#
# 001
# 023
# 002
# 017
# 102
# Write a function that takes a variable number of integers and returns the string to be printed out.

def print_nums(*args):
    if not args:
        return ""
    l = len(str(max(args)))
    result = []
    for i in args:
        if len(str(i)) < l:
            result.append(('0' * (l - len(str(i)))) + str(i))
        else:
            result.append(str(i))
    return '\n'.join(result)