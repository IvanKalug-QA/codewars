# Given a string, return a new string that has transformed based on the input:
#
# Change case of every character, ie. lower case to upper case, upper case to lower case.
# Reverse the order of words from the input.
# Note: You will have to handle multiple spaces, and leading/trailing spaces.
#
# For example:
#
# "Example Input" ==> "iNPUT eXAMPLE"
# You may assume the input only contain English alphabet and spaces.

def string_transformer(s):
    if not len(s):
        return ''
    l = list()
    st = ''
    for i in s.split(' '):
        st = ''
        for j in i:
            if j.isupper():
                st += j.lower()
            elif j.islower():
                st += j.upper()
            else:
                st += j
        l.append(st)
    return ' '.join(l[::-1])