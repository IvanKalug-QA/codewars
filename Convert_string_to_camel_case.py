# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
#
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    if not len(text):
        return ''
    l = []
    res = list()
    s = ''
    for i in text:
        if i.isalpha():
            s += i
        else:
            l.append(s)
            s = ''
    if len(s):
        l.append(s)
    for i in l[1::]:
        res.append(i.title())
    return l[0] + ''.join(res)