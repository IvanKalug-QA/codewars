# Given any number of boolean flags function should return true if and only if one of them is true while others are false. If function is called without arguments it should return false.
#
#   only_one() == False
#   only_one(True, False, False) == True
#   only_one(True, False, False, True) == False
#   only_one(False, False, False, False) == False

def only_one(*args):
    if not args:
        return False
    tru = 0
    for i in args:
        if i == True:
            tru += 1
    return tru == 1