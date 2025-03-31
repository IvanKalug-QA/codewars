# Given that
#
# f0 = '0'
# f1 = '01'
# f2 = '010' = f1 + f0
# f3 = '01001' = f2 + f1
# You will be given a number and your task is to return the nth fibonacci string. For example:
#
# solve(2) = '010'
# solve(3) = '01001'
# More examples in test cases. Good luck!
#
# If you like sequence Katas, you will enjoy this Kata: Simple Prime Streaming

def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    f0 = '0'
    f1 = '01'
    for i in range(2, n + 1):
        f0, f1 = f1, f1 + f0,
    return f1