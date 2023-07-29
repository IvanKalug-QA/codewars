# DESCRIPTION:
# Implement a function that returns the minimal and the maximal value of a list (in this order).

def get_min_max(seq):
    l = []
    l.append(min(seq))
    l.append(max(seq))
    return tuple(l)