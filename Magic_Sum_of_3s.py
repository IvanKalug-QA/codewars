# The magic sum of 3s is calculated on an array by summing up odd numbers which include the digit 3.
#
# Complete the function which accepts an array of integers and returns its magic sum of 3s.
#
# Example: [3, 12, 5, 8, 30, 13] results in 16 (3 + 13)
#
# If there is no such number in the array, 0 should be returned.

def magic_sum(arr):
    s = 0
    for i in arr:
        if i % 2 != 0 and "3" in str(i):
            s += i
    return s