# Complete the function that accepts a valid string and returns an integer.
#
# Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of the numbers in the hex strings (ignore letters).
#
# Examples
# "Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
# "Hello, World!"  ==> 91
# "Forty4Three"    ==> 113

from string import digits
def hex_hash(code):
    l = list()
    for i in code:
        l.append(ord(i))
    count = 0
    for i in l:
        for j in hex(i)[2:]:
            if j in digits:
                count += int(j)
    return count