# In this kata, you will do addition and subtraction on a given string. The return value must be also a string.
#
# Note: the input will not be empty.
#
# Examples
# "1plus2plus3plus4"  --> "10"
# "1plus2plus3minus4" -->  "2"

def calculate(s):
    stack_dig = []
    stack_command = []
    st = ''
    com = ''
    for i in range(len(s)):
        if s[i].isdigit():
            st += s[i]
        else:
            if st:
                stack_dig.append(int(st))
                st = ''
    else:
        if st:
            stack_dig.append(int(st))
    stack_dig = stack_dig[::-1]
    for i in s:
        if i.isalpha():
            com += i
        else:
            if com:
                stack_command.append(com)
            com = ''
    for i in stack_command:
        if i == 'plus':
            stack_dig.append(stack_dig.pop() + stack_dig.pop())
        elif i == 'minus':
            stack_dig.append(stack_dig.pop() - stack_dig.pop())
    return str(stack_dig.pop())