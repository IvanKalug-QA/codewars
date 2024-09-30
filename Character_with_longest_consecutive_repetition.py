# DESCRIPTION:
# For a given string s find the character c (or C) with longest consecutive repetition and return:
#
# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
#
# For empty string return:
#
# ('', 0)
# Happy coding! :)

def longest_repetition(chars):
    if not chars:
        return ('', 0)
    res = []
    counter = 0
    cur = chars[0]
    for i in chars:
        if i == cur:
            counter += 1
        else:
            res.append((cur, counter))
            cur = i
            counter = 1
    res.append((cur, counter))
    return sorted(res, key=lambda x: x[1], reverse=True)[0]