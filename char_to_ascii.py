# Take a string and return a hash with all the ascii values of the characters in the string. Returns nil (Ruby), None (Python) or null (JavaScript) if the string is empty. The key is the character, and the value is the ascii value of the character. Repeated characters are to be ignored and non-alphebetic characters as well.


def char_to_ascii(s):
    if not s:
        return
    d = {}
    for i in s:
        if i.isalpha() and i not in d:
            d[i] = ord(i)
    return d