# Your task is to write a function, which takes two arguments and returns a sequence. First argument is a sequence of values, second is multiplier. The function should filter all non-numeric values and multiply the rest by given multiplier.

def multiply_and_filter(seq, multiplier):
    l = list()
    for i in seq:
        if type(i) != bool and (isinstance(i, int) or isinstance(i, float)):
            l.append(i * multiplier)
    return l
