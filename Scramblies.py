# DESCRIPTION:
# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    s1_chars = {}
    s2_chars = {}

    for char in s1:
        s1_chars[char] = s1_chars.get(char, 0) + 1

    for char in s2:
        s2_chars[char] = s2_chars.get(char, 0) + 1

    for char, count in s2_chars.items():
        if s1_chars.get(char, 0) < count:
            return False
    return True