# Find the number with the most digits.
#
# If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    k = 0
    v = 0
    for i in arr:
        if len(str(i)) > k:
            k = len(str(i))
            v = i
    return v