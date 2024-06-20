# Compare two strings by comparing the sum of their values (ASCII character code).
#
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.
#
# Examples:
# "AD", "BC"  -> equal
# "AD", "DD"  -> not equal
# "gf", "FG"  -> equal
# "zz1", ""   -> equal (both are considered empty)
# "ZzZz", "ffPFF" -> equal
# "kl", "lz"  -> not equal
# null, ""    -> equal

def compare(s1, s2):
    if not s1 or not s2:
        return True
    count1 = 0
    count2 = 0
    if type(s1) == list:
        return False
    else:
        for i in s1.upper():
            if i.isalpha():
                count1 += ord(i)
            else:
                count1 = 0
                break
    if type(s2) == list:
        return False
    else:
        for i in s2.upper():
            if i.isalpha():
                count2 += ord(i)
            else:
                count2 = 0
                break
    print(count1, count2)
    return count1 == count2