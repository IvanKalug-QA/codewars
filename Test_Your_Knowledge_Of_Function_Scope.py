# Write a function that adds from two invocations.
#
# All inputs will be integers.
#
# add(3)(4)  // 7
# add(12)(20) // 32

def add(a):
    n = a
    def appendd(f):
        return n + f
    return appendd