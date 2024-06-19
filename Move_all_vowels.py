# Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.
#
# Vowels are (in this kata): a, e, i, o, u
#
# Note: all provided input strings are lowercase.
#
# Examples
# "day"    ==>  "dya"
# "apple"  ==>  "pplae"

def move_vowels(input):
    l = list()
    volwels = list()
    for i in input:
        if i in ['a', 'e', 'i', 'o', 'u']:
            volwels.append(i)
        else:
            l.append(i)
    return ''.join(l+volwels)
