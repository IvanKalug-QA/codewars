# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    w = ''
    for i in s:
        if i.isupper():
            w += "*" + i
        else:
            w += i
    return ' '.join(w.split('*'))