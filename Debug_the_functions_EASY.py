# Should be easy, begin by looking at the code. Debug the code and the functions should work.
#
# There are three functions: Multiplication (x) Addition (+) and Reverse (!esreveR)

def multi(l_st):
    c = 1
    for i in l_st:
        c *= i
    return c
def add(l_st):
    c = 0
    for i in l_st:
        c+=i
    return c
def reverse(string):
    l = []
    for i in string.split():
        l += [i[::-1]]
    return ' '.join(l[::-1])