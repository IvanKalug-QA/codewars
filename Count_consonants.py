# DESCRIPTION:
# Complete the function that takes a string of English-language text and returns the number of consonants in the string.
#
# Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

def consonant_count(s):
    n = 0
    for i in s:
        if i.lower() in "bcdfghjklmnpqrstvwxyz":
            n += 1
    return n