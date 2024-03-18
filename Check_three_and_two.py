# Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), check if the array contains three and two of the same values.
#
# Examples
# ["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
# ["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
# ["a", "a", "a", "a", "a"] ==> false // 5x "a"

def check_three_and_two(array):
    d = dict()
    for i in array:
        d[i] = d.get(i, 0) + 1
    c = 0
    flag = True
    for i in d:
        if d[i] == 2 and flag:
            c += 1
            flag = False
        elif d[i] == 3:
            c += 1
    return c == 2