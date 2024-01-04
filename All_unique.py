# Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.
#
# The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

def has_unique_chars(string):
    d = dict()
    for i in string:
        d[i] = d.get(i, 0) + 1
    for i in d:
        if d[i] > 1:
            return False
    return True