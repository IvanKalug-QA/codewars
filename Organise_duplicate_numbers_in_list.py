# am is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.
#
# Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:
#
# group([3, 2, 6, 2, 1, 3])
# >>> [[3, 3], [2, 2], [6], [1]]
# Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.

def group(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] == '':
            continue
        array = [arr[i]]
        for j in range(i+1, len(arr)):
            if arr[j] != '':
                if arr[j] == arr[i]:
                    array.append(arr[j])
                    arr[j] = ''
        res.append(array)
        arr[i] = ''
    return res