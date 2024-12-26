# Move every letter in the provided string forward 10 letters through the alphabet.
#
# If it goes past 'z', start again at 'a'.
#
# Input will be a string with length > 0.

from string import ascii_lowercase
def move_ten(st):
    return ''.join([ascii_lowercase[(ascii_lowercase.index(i) + 10) % 26] for i in st])