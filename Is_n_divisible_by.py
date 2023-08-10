# DESCRIPTION:
# Create a function that checks if the first argument n is divisible by all other arguments (return true if no other arguments)
#
# Example:
#
# (6,1,3)--> true because 6 is divisible by 1 and 3
# (12,2)--> true because 12 is divisible by 2
# (100,5,4,10,25,20)--> true
# (12,7)--> false because 12 is not divisible by 7
# This kata is following kata: http://www.codewars.com/kata/is-n-divisible-by-x-and-y

def is_divisible(*args):
    l = [*args]
    f = l[0]
    l = l[1::]
    for i in l:
        if f % i != 0:
            return False
    return True