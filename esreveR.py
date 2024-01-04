# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)
#
# (the dedicated builtin(s) functionalities are deactivated)

def reverse(lst):
    l = list()
    for i in range(1, len(lst) + 1):
        l.append(lst[-i])
    return l