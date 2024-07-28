# Write a function with the signature shown below:
#
# def is_int_array(arr):
#     return True
# returns true  / True if every element in an array is an integer or a float with no decimals.
# returns true  / True if array is empty.
# returns false / False for every other input.

def is_int_array(arr):
    if arr is None or arr == '' or type(arr) != list:
        return False
    if arr == []:
        return True
    count = 0
    for i in arr:
        if type(i) == float and str(i).split('.')[-1] == '0':
            count += 1
        elif i is None:
            break
        elif type(i) == int and i % i == 0:
            count += 1
    if count == len(arr):
        return True
    return False