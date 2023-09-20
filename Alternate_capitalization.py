# DESCRIPTION:
# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.
#
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
#
# The input will be a lowercase string with no spaces.
#
# Good luck!

def capitalize(s):
    l = []
    f = ''
    for i in range(len(s)):
        if i % 2 == 0:
            f += s[i].upper()
        else:
            f += s[i]
    l.append(f)
    l.append(f.swapcase())
    return l