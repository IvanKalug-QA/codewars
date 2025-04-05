# You need to write a function, that returns the first non-repeated character in the given string.
#
# If all the characters are unique, return the first character of the string.
# If there is no unique character, return null in JS or Java, None in Python, '\0' in C.
#
# You can assume, that the input string has always non-zero length.
#
# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns null (all the characters are repeated)

from collections import Counter
def first_non_repeated(s):
    count = Counter(s)
    for i in s:
        if count[i] == 1:
            return i
    return None