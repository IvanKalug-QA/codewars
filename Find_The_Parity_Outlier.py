# DESCRIPTION:
# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(inte):
    l1 = []
    l2 = []
    for i in inte:
        if i % 2 == 0:
            l1.append(i)
        elif i % 2 != 0:
            l2.append(i)
    if len(l1) == 1:
        return l1[0]
    else:
        return l2[0]