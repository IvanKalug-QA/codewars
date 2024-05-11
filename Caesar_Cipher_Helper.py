# Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.
#
# For example:
#
# c = CaesarCipher(5); # creates a CipherHelper with a shift of five
# c.encode('Codewars') # returns 'HTIJBFWX'
# c.decode('BFKKQJX') # returns 'WAFFLES'
# If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
# The shift will always be in range of [1, 26].

import string


class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        encrypt = ''
        for i in st:
            if i in uppercase:
                new = (uppercase.index(i) + self.shift) % 26
                encrypt += uppercase[new]
            elif i in lowercase:
                new = (lowercase.index(i) + self.shift) % 26
                encrypt += lowercase[new]
            else:
                encrypt += i
        return encrypt.upper()

    def decode(self, st):
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        decrypt = ''
        for i in st:
            if i in uppercase:
                last = (uppercase.index(i) - self.shift) % 26
                decrypt += uppercase[last]
            else:
                decrypt += i
        return decrypt