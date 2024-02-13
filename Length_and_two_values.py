# Given an integer n and two other values, build an array of size n filled with these two values alternating.
#
# Examples
# 5, true, false     -->  [true, false, true, false, true]
# 10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
# 0, "one", "two"    -->  []
# Good luck!

def alternate(n, first_value, second_value):
    if n == 0:
        return []
    l = list()
    l.append(first_value)
    m = first_value
    for i in range(n - 1):
        if m == first_value:
            l.append(second_value)
            m = second_value
        else:
            l.append(first_value)
            m = first_value
    return l