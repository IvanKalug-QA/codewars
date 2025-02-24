# Description:
# Write a function that doubles every second integer in a list, starting from the left.
#
# Example:
#
# For input array/list :
#
# [1,2,3,4]
# the function should return :
#
# [1,4,3,8]
def double_every_other(lst):
    for i in range(1, len(lst), 2):
        lst[i] = lst[i] * 2
    return lst