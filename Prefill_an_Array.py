# Create the function prefill that returns an array of n elements that all have the same value v. See if you can do this without using a loop.
#
# You have to validate input:
#
# v can be anything (primitive or otherwise)
# if v is ommited, fill the array with undefined
# if n is 0, return an empty array
# if n is anything other than an integer or integer-formatted string (e.g. '123') that is >=0, throw a TypeError
# When throwing a TypeError, the message should be n is invalid, where you replace n for the actual value passed to the function.
#
# Code Examples
#
#     prefill(3,1) --> [1,1,1]
#
#     prefill(2,"abc") --> ['abc','abc']
#
#     prefill("1", 1) --> [1]
#
#     prefill(3, prefill(2,'2d'))
#       --> [['2d','2d'],['2d','2d'],['2d','2d']]
#
#     prefill("xyz", 1)
#       --> throws TypeError with message "xyz is invalid"

from string import digits
def prefill(n,v='undefined'):
    if type(n) == str and '.' not in n and n[0] in digits:
        return int(n) * [v]
    elif type(n) == int:
        return n * [v]
    raise TypeError(f'{n} is invalid')