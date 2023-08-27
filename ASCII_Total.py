# DESCRIPTION:
# You'll be given a string, and have to return the sum of all characters as an int. '
# 'The function should be able to handle all printable ASCII characters.
#
# Examples:
#
# uniTotal("a") == 97
# uniTotal("aaa") == 291

def uni_total(s):
    if not s:
        return 0
    count = 0
    for i in s:
        count += ord(i)
    return count