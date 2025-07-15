# Task
# Tranform of input array of zeros and ones to array in which counts number of continuous ones. If there is none, return an empty array
#
# Example
# [1, 1, 1, 0, 1] -> [3,1]
# [1, 1, 1, 1, 1] -> [5]
# [0, 0, 0, 0, 0] -> []

def ones_counter(inp):
    counter = 0
    result = []
    for i in inp:
        if i == 0:
            if counter > 0:
                result.append(counter)
            counter = 0
        else:
            counter += 1
    if counter > 0:
        result.append(counter)
    return result