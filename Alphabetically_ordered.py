# Your task is very simple. Just write a function that takes an input string of lowercase letters and returns true/false depending on whether the string is in alphabetical order or not.
#
# Examples (input -> output)
# "kata" -> false ('a' comes after 'k')
# "ant" -> true (all characters are in alphabetical order)
# Good luck :)

from string import ascii_lowercase
def alphabetic(s):
    for i in range(len(s) - 1):
        if ascii_lowercase.index(s[i]) > ascii_lowercase.index(s[i+1]):
            return False
    return True