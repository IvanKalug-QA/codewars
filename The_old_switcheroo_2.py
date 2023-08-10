# DESCRIPTION:
# This is a follow up from my kata The old switcheroo
#
# Write the function :
#
# def encode(str)
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
#
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'
# String are case sensitive.

def encode(string):
    dict = {'a': 1, 'b': 2, 'c': 3,
            'd': 4, 'e': 5, 'f': 6,
            'g': 7, 'h': 8, 'i': 9,
            'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18,
            's': 19, 't': 20, 'u': 21,
            'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26}
    string = string.lower()
    for i in string:
        if i.isalpha():
            c = dict[i]
            string = string.replace(i,str(c))
    return string