# Complete the solution so that it returns a formatted string. The return value should equal "Value is VALUE" where value is a 5 digit padded number.
#
# Example:
#
# solution(5)  # should return "Value is 00005"

def solution(value):
    if value == 0:
        return 'Value is 00000'
    elif len(str(value)) == 1:
        return 'Value is ' + '0000' + str(value)
    elif len(str(value)) == 2:
        return 'Value is ' + '000' + str(value)
    elif len(str(value)) == 3:
        return 'Value is ' + '00' + str(value)
    elif len(str(value)) == 4:
        return 'Value is ' + '0' + str(value)
    return 'Value is ' + str(value)