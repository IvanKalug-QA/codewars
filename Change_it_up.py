# Create a function that takes a string as a parameter and does the following, in this order:
#
# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:
#
# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
# So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)

def changer(s):
    d = {'a': 1, 'b': 2, 'c': 3,
     'd': 4, 'e': 5, 'f': 6,
     'g': 7, 'h': 8, 'i': 9,
     'j': 10, 'k': 11, 'l': 12,
     'm': 13, 'n': 14, 'o': 15,
     'p': 16, 'q': 17, 'r': 18,
     's': 19, 't': 20, 'u': 21,
     'v': 22, 'w': 23, 'x': 24,
     'y': 25, 'z': 26}
    res = {1: 'a', 2: 'b', 3: 'c',
     4: 'd', 5: 'e', 6: 'f',
     7: 'g', 8: 'h', 9: 'i',
     10: 'j', 11: 'k', 12: 'l',
     13: 'm', 14: 'n', 15: 'o',
     16: 'p', 17: 'q', 18: 'r',
     19: 's', 20: 't', 21: 'u',
     22: 'v', 23: 'w', 24: 'x',
     25: 'y', 26: 'z'}
    l = list()
    for i in s:
        if i.isalpha():
            if d[i.lower()] == 26:
                l.append('a')
            else:
                l.append(res[d[i.lower()] + 1])
        else:
            l.append(i)
    for i in range(len(l)):
        if l[i] in ('a', 'o', 'e', 'i', 'u'):
            l[i] = l[i].upper()
    return ''.join(l)