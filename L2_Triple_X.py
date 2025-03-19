# Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".
#
# "abraxxxas" → true
# "xoxotrololololololoxxx" → false
# "softX kitty, warm kitty, xxxxx" → true
# "softx kitty, warm kitty, xxxxx" → false
# Note :
#
# capital X's do not count as an occurrence of "x".
# if there are no "x"'s then return false

def triple_x(s):
    result = []
    st = ''
    for i in s:
        if i != 'x':
            if st:
                result.append(st)
            st = ''
        elif i == 'x':
            st += i
    else:
        if st: result.append(st)
    return True if result and len(result[0]) >= 3 else False