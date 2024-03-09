# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.
#
# Solve("*'&ABCDabcde12345") = [4,5,5,3].
# --the order is: uppercase letters, lowercase, numbers and special characters.
# More examples in the test cases.
#
# Good luck!

def solve(s):
    uppercase = 0
    lowercase = 0
    numbers = 0
    special = 0
    for i in s:
        if i.isalpha():
            if i.isupper():
                uppercase += 1
            else:
                lowercase += 1
        elif i.isdigit():
            numbers += 1
        else:
            special += 1
    return [uppercase, lowercase, numbers, special]