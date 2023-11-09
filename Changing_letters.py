# When provided with a String, capitalize all vowels
#
# For example:
#
# Input : "Hello World!"
#
# Output : "HEllO WOrld!"
#
# Note: Y is not a vowel in this kata.


def swap(st):
    s = ''
    if st[0].isupper():
        s += st[0]
        r = st[1::]
        for i in r:
            if i in ['a', 'o', 'e', 'i', 'u']:
                s += i.upper()
            else:
                s += i
    else:
        for i in st:
            if i in ['a', 'o', 'e', 'i', 'u']:
                s += i.upper()
            else:
                s += i
    return s