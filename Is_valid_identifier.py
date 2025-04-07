# Given a string, determine if it's a valid identifier.
#
# Here is the syntax for valid identifiers:
# Each identifier must have at least one character.
# The first character must be picked from: alpha, underscore, or dollar sign. The first character cannot be a digit.
# The rest of the characters (besides the first) can be from: alpha, digit, underscore, or dollar sign. In other words, it can be any valid identifier character.
# Examples of valid identifiers:
# i
# wo_rd
# b2h
# Examples of invalid identifiers:
# 1i
# wo rd
# !b2h

from string import digits
def is_valid(idn):
    if len(idn) < 1:
        return False
    elif not idn[0].isalpha() and idn[0] not in {'_', '$'}:
        return False
    for i in range(1, len(idn)):
        if not idn[i].isalpha() and idn[i] not in {'_', '$'} and idn[i] not in digits:
            return False
    return True