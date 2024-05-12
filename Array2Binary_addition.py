# Given an array containing only integers, add all the elements and return the binary equivalent of that sum.
#
# If the array contains any non-integer element (e.g. an object, a float, a string and so on), return false.
#
# Note: The sum of an empty array is zero.
#
# arr2bin([1,2]) == '11'
# arr2bin([1,2,'a']) == False

def arr2bin(arr):
    count = 0
    for i in arr:
        if type(i) == str or type(i) == float or type(i) == list or type(i) == bool:
            return False
        count += i
    return bin(count)[2::]