# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!
#
# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes
# A hyphen will separate the two letters in the string.
# You don't need to worry about error handling in this kata (i.e. both letters will be the same case and the second letter will not be before the first alphabetically).

from string import ascii_lowercase, ascii_uppercase
def gimme_the_letters(sp):
    sp = sp.split('-')
    result = []
    if sp[0].isupper():
        for i in range(ascii_uppercase.index(sp[0]), len(ascii_uppercase)):
            if sp[-1] == ascii_uppercase[i]:
                result.append(ascii_uppercase[i])
                return ''.join(result)
            else:
                result.append(ascii_uppercase[i])
        else:
            return ''.join(result)
    else:
        for i in range(ascii_lowercase.index(sp[0]), len(ascii_lowercase)):
            if sp[-1] == ascii_lowercase[i]:
                result.append(ascii_lowercase[i])
                return ''.join(result)
            else:
                result.append(ascii_lowercase[i])
        else:
            return ''.join(result)