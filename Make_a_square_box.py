# Easy; Make a box
# Given a number as a parameter (between 2 and 30), return an array containing strings which form a box.
# Like this:

# n = 5

# [
#   '-----',
#   '-   -',
#   '-   -',
#   '-   -',
#   '-----'
# ]
# n = 3

# [
#   '---',
#   '- -',
#   '---'
# ]

def box(n):
    border = '-' * n
    middle = '-' + ' ' * (n - 2) + '-'
    result = [border]
    for i in range(n - 2):
        result.append(middle)
    result.append(border)
    
    return result