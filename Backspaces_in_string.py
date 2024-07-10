# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    if not len(s):
        return ""
    stack  = list()
    for i in s:
        if i.isalpha():
            stack.append(i)
        elif i == '#':
            if len(stack):
                stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)