# Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.
#
# Note: Booleans should not be considered as numbers.

def cube_odd(arr):
    l = list()
    for i in arr:
        if type(i) != int:
            return None
        elif (i**3) % 2 != 0:
            l.append(i**3)
    return sum(l)