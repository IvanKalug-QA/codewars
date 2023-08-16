# DESCRIPTION:
# Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.
#
# Examples
# "312" should return "333122"
# "102269" should return "12222666666999999999"

def explode(s):
    st = ''
    for i in s:
        c = int(i)
        st += i * c
    return st