# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    result = []
    idx = -1
    for i in range(len(strng) - 1, -1, -1):
        if strng[i].isdigit():
            result.append(int(strng[i]))
        else:
            idx = i
            break
    if not result:
        result.append(0)
    remains = 0
    add_one = False
    for i in range(len(result)):
        if not add_one:
            add = result[i] + 1
            if len((str(add))) == 2:
                remains = add // 10
            result[i] = add % 10 if len((str(add))) == 2 else add
            add_one = True
        else:
            if remains == 0:
                break
            add = result[i] + remains
            if len((str(add))) == 2:
                remains = add // 10
            else:
                remains = 0
            result[i] = add % 10 if len((str(add))) == 2 else add
    if remains != 0:
        result.append(remains)
    return strng[0:idx + 1] + ''.join(str(i) for i in result[::-1])