# When given a string of space separated words, return the word with the longest length. If there are multiple words with the longest length, return the last instance of the word with the longest length.
#
# Example:
#
# 'red white blue' //returns string value of white
#
# 'red blue gold' //returns gold

def longest_word(s):
    l = list()
    for i in s.split():
        l.append([len(i), i])
    c = 0
    r = ''
    for i in l[::-1]:
        if i[0] > c:
            c = i[0]
            r = i[1]
    return r