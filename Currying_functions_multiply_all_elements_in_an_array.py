# To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array of integers as an argument. This function must return another function, which takes a single integer as an argument and returns a new array.
#
# The returned array should consist of each of the elements from the first array multiplied by the integer.
#
# Example:
#
# multiply_all([1, 2, 3])(2); // => [2, 4, 6]
# You must not mutate the original array.
#
# Here's a nice Youtube video about currying, which might help you if this is new to you.

def multiply_all(x):
    l = x
    def multipyAll(r):
        f  = []
        for i in l:
            f.append(i * r)
        return f
    return multipyAll