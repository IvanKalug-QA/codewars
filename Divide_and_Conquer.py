# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
#
# Return as a number.

def div_con(x):
    c = 0
    y = 0
    for i in x:
        if type(i) == int:
            c += i
        else:
            y += int(i)
    return c - y