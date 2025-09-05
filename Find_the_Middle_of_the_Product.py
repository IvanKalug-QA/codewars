# Given a string of characters, create a function returning the middle number in the product of each digit in the string.
#
# Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.
#
# Not all strings will contain digits and not all inputs will be string. In those cases, return -1.
#
# If the product has an even number of digits, return the middle two digits
#
# Example: 1563 -> 56
#
# NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1

def find_middle(st):
    if not isinstance(st, str):
        return -1
    re = 1
    for i in st:
        if i.isdigit():
            re *= int(i)
    m = len(str(re)) // 2
    if len(str(re)) % 2 == 0:
        return int(str(re)[m-1] + str(re)[m])
    return int(str(re)[m])