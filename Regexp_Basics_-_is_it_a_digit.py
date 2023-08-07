# DESCRIPTION:
# Implement String digit? (in Java StringUtils.isDigit(String)),
# which should return true if given object is a digit (0-9), false otherwise.

def is_digit(n):
    if n.isnumeric():
        if int(n) in [0,1,2,3,4,5,6,7,8,9]:
            return True
    return False