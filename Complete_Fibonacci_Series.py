# The function 'fibonacci' should return an array of fibonacci numbers. The function takes a number as an argument to decide how many no. of elements to produce. If the argument is less than or equal to 0 then return empty array
#
# Example:
#
# fibonacci(4) # should return  [0,1,1,2]
# fibonacci(-1) # should return []

ef fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    array = [0, 1]
    while len(array) < n:
        array.append(array[-2] + array[-1])
    return array