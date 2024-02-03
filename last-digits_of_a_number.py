# Your job is to implement a function which returns the last D digits of an integer N as a list.
#
# Special cases:
# If D > (the number of digits of N), return all the digits.
# If D <= 0, return an empty list.
# Examples:
# N = 1
# D = 1
# result = [1]
#
# N = 1234
# D = 2
# result = [3, 4]
#
# N = 637547
# D = 6
# result = [6, 3, 7, 5, 4, 7]

def solution(n,d):
    l = [int(i) for i in str(n)]
    if d >= len(l) or len(l) == 1:
        return l
    elif d <= 0:
        return []
    l1 = list()
    c = 0
    for i in l[::-1]:
        if c == d:
            return l1[::-1]
        else:
            c += 1
            l1.append(i)