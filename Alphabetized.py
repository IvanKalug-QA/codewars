# The alphabetized kata
# Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!
#
# The input is restricted to contain no numerals and only words containing the english alphabet letters.
#
# Example:
#
# alphabetized("The Holy Bible") # "BbeehHilloTy"

def alphabetized(s):
    l = list()
    for i in s:
        if i.isalpha():
            l.append(i)
    s = sorted(''.join(l), key=lambda x: x.lower())
    return ''.join(s)