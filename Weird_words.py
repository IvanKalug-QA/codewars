# Change every letter in a given string to the next letter in the alphabet. The function takes a single parameter s (string).
#
# Notes:
#
# Spaces and special characters should remain the same.
# Capital letters should transfer in the same way but remain capitilized.
# Examples
# "Hello"               -->  "Ifmmp"
# "What is your name?"  -->  "Xibu jt zpvs obnf?"
# "zoo"                 -->  "app"
# "zzZAaa"              -->  "aaABbb"

from string import ascii_lowercase, ascii_uppercase
def next_letter(s):
    result = []
    for i in s:
        if i.isalpha():
            if i == 'z':
                result.append('a')
            elif i in ascii_lowercase:
                result.append(ascii_lowercase[(ascii_lowercase.index(i) + 1) % 26])
            elif i in ascii_uppercase:
                result.append(ascii_uppercase[(ascii_uppercase.index(i) + 1) % 26])
        else:
            result.append(i)
    return ''.join(result)