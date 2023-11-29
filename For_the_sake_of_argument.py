# Write a function named numbers.
#
# function should return True if all the parameters it is passed are of the integer type or float type. Otherwise, the function should return False.
#
# The function should accept any number of parameters.
#
# Example usage:
#
# numbers(1, 4, 3, 2, 5); # True
# numbers(1, "a", 3); # False
# numbers(1, 3, None); # False
# numbers(1.23, 5.6, 3.2) # True

def numbers(*args):
    count = 0
    for i in [*args]:
        if type(i) == int or type(i) == float:
            count += 1
        else:
            return False
    return True