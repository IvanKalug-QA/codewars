# DESCRIPTION:
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
#
# Note: anagrams are case insensitive
#
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
#
# Examples
# "foefet" is an anagram of "toffee"
#
# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    f = len(original)
    count = 0
    if len(test) == len(original):
        for i in test.lower():
            if i in original.lower():
                count += 1
            else:
                count += 0
        if count == f:
            return True
        return False
    return False