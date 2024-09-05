# Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.
#
# Ex:
#
# 274 -> '2-7-4'
# 6815 -> '68-1-5'


def dashatize(n):
    res = list()
    s = ''
    for i in str(abs(n)):
        if int(i)%2==0:
            s += i
        else:
            if s != '':
                res.append(s)
            res.append(i)
            s = ''
    res.append(s)
    return '-'.join(res)[:-1] if '-'.join(res)[-1] == '-' else '-'.join(res)