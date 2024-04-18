# Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last index.
#
# Indices in sequence start from 0.
#
# If the sequence is empty, you should return 0.

def even_last(numbers):
    if not numbers:
        return 0
    l = list()
    for i, v in enumerate(numbers):
        if i % 2 == 0:
            l.append(v * numbers[-1])
    return sum(l)