# DESCRIPTION:
# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    li = []
    for i in s.split():
        li.append(len(i))
    return min(li) # l: shortest word length