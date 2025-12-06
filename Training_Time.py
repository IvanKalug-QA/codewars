# Task
# Complete the function that accepts two or more parameters. The first parameter is an array of numbers, followed by an arbitrary number of numeric arrays. Each numeric array contains two numbers, which are indices for elements in arr (the numbers will always be within bounds). For every such array, swap the elements.

# For a detailed explanation of arrow functions (JS only), the spread operator, destructuring, and rest parameters, scroll down.

# Examples
# [1, 2, 3, 4, 5], [1, 2]  should return  [1, 3, 2, 4, 5]
#     <-->

# [1, 2, 3, 4, 5], [1, 2], [3, 4]  should return  [1, 3, 2, 5, 4]
#     <-->
#           <-->

# [1, 2, 3, 4, 5], [1, 2], [3, 4], [2, 3]  should return  [1, 3, 5, 2, 4]
#     <-->
#           <-->
#        <-->
# The Spread Operator
# Another skill is the spread operator. The spread operator allows an expression to be expanded in places where multiple arguments (for function calls) or multiple elements (for array literals) are expected. It can be used in multiple places:

# In function calls:
# def plus(a, b, c, d, e):
#     return a + b + c + d + e

# arg1 = [1, 2, 3, 4, 5]
# print(plus(*arg1)) # output is 15
# ...arg1 spreads all the elements in arg1 into individual parameters to plus(). In Javascript, it's also possible to use the spread operator in the middle of a parameter list, as was done with ...arg2.

# Ok, the lesson is over. Did you get it all? Let's do the task now.

def shuffle_it(l, *args):
    if not args:
        return l
    for s, e in args:
        l[s], l[e] = l[e], l[s]
    return l