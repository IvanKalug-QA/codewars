# DESCRIPTION:
# Is it possible to write a book without the letter 'e' ?
#
# Task
# Given String str, return:
#
# How many "e" does it contain (case-insensitive) in string format.
# If given String doesn't contain any "e", return: "There is no "e"."
# If given String is empty, return empty String.
# If given String is `null`/`None`/`nil`, return `null`/`None`/`nil`

def find_e(s):
    if s is None:
        return None
    elif not s:
        return ''
    d = dict()
    for i in s.lower():
        if i == 'e':
            d[i] = d.get(i, 0) + 1
    return str(d['e']) if d.get('e', False) else 'There is no "e".'