# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
#
# Example:
#
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    l = list()
    for i in s:
        if i == 'a':
            l.append('b')
        elif i == 'b':
            l.append('a')
        else:
            l.append(i)
    return ''.join(l)