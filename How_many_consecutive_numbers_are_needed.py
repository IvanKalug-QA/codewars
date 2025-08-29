# Write a function that takes an array of unique integers and returns the minimum number of integers needed to make the values of the array consecutive from the lowest number to the highest number.
#
# Example
# [4, 8, 6] --> 2
# Because 5 and 7 need to be added to have [4, 5, 6, 7, 8]
#
# [-1, -5] --> 3
# Because -2, -3, -4 need to be added to have [-5, -4, -3, -2, -1]
#
# [1] --> 0
# []  --> 0

def consecutive(arr):
    if len(arr) < 2:
        return 0
    counter = 0
    mi, ma = min(arr), max(arr)
    for i in range(mi, ma):
        if i not in arr:
            counter += 1
    return counter