# Task & Rules
# Give you an array arr that contains some number elements, find out the peaks and valleys in the array, and return them.

# What do the peaks and valleys mean? If an element is larger than the three one on the left and larger than the three one on the right, we call it a peak. In contrast, an element is smaller than the value of the three elements(left and right), we call it a valley. an example:

# [10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]
# In the example above, peaks and valleys are:

# [10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]

# [         40   ,   10        ,       16         ]
# Some examples:
# [10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]
# => [40,10,16]

# [50,84,49,47,80,87,87,53,76,30,10]
# => [47]

# [45,94,41,76,29,96,28,13,84,69,25]
# => [96,13]

# [1,16,63,78,53,78,42,39,46,88,49,96,58,82]
# => [39]

# [45,75,47,44,93,95,31,99,49,48,76,2,92,23,26,19,60,45,51]
# => [31,99,2,92,19]

# [49,97,76,56,96,88,65,20,14,93,32]
# => []

def peak_and_valley(arr):
    result = []
    n = len(arr)
    if n < 7:
        return result
    for i in range(3, n - 3):
        is_peak = all(arr[i] > arr[i - j] for j in range(1, 4)) and \
                  all(arr[i] > arr[i + j] for j in range(1, 4))
        is_valley = all(arr[i] < arr[i - j] for j in range(1, 4)) and \
                    all(arr[i] < arr[i + j] for j in range(1, 4))
        if is_peak or is_valley:
            result.append(arr[i])
    return result