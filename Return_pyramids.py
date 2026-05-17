# The task is very simple: you must return pyramids. Given a number n, you build a pyramid with n floors

# For example , given a n=4 you must to print this pyramid:

#    /\
#   /  \
#  /    \
# /______\ 
# Other example, given a n=6 you must to print this pyramid:

#      /\
#     /  \
#    /    \
#   /      \
#  /        \
# /__________\
# Another example, given a n=10, you must to print this pyramid:

#          /\
#         /  \
#        /    \
#       /      \
#      /        \
#     /          \
#    /            \
#   /              \
#  /                \
# /__________________\
# Note: a line feed character is needed at the end of the string.

def pyramid(n):
    result = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        if i == n - 1:
            result.append(spaces + '/' + '_' * (2 * i) + '\\')
        else:
            result.append(spaces + '/' + ' ' * (2 * i) + '\\')
    return '\n'.join(result) + '\n'