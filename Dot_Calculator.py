# Dot Calculator
# You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.
#
# Here are the following valid operators :
#
# + Addition
# - Subtraction
# * Multiplication
# // Integer Division
# Your Work (Task)
# You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction, the first number will always be greater than or equal to the second number.
#
# Examples (Input => Output)
# * "..... + ..............." => "...................."
# * "..... - ..."             => ".."
# * "..... - ."               => "...."
# * "..... * ..."             => "..............."
# * "..... * .."              => ".........."
# * "..... // .."             => ".."
# * "..... // ."              => "....."
# * ". // .."                 => ""
# * ".. - .."                 => ""

def calculator(txt):
    a = txt.split()[0]
    b = txt.split()[1]
    c = txt.split()[2]
    if b == '+':
        r = len(a)+len(c)
        return '.' * r
    elif b == '-':
        r = len(a)-len(c)
        if r > 0:
            return '.' * r
        else:
            return ''
    elif b == '//':
        r = len(a)//len(c)
        if r > 0:
            return '.' * r
        else:
            return ''
    else:
        r = len(a)*len(c)
        return '.' * r