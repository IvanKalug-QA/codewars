# Reverse and invert all integer values in a given list.
#
# [1,12,'a',3.4,87,99.9,-42,50,5.6] --> [-1,-21,-78,24,-5]
# Remove all types other than integer.

def reverse_invert(lst):
    result = []
    for i in lst:
        if isinstance(i, int):
            if i < 0:
                result.append(int(str(abs(i))[::-1]))
            else:
                result.append(-int(str(abs(i))[::-1]))
    return result