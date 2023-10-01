# DESCRIPTION:
# In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
#
# The string has the following conditions to be alphanumeric:
#
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore

def alphanumeric(password):
    count = 0
    if len(password) == 0:
        return False
    for i in password:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            count += 1
    return False if len(password) != count else True