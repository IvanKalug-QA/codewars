# Write a function that takes two arguments:
#
# An array: The array to be split into smaller parts.
# Chunk size: A positive integer, which is the size of each chunk.
# This function should split the given array into parts with the given chunk size, and return the result as a nested array.
#
# If the array cannot be evenly divided by the size, the last part may contain fewer elements.
#
# If an array of size 123 is given and the chunk size is 10, the function will split the array into 13 smaller parts:
#
# The first 12 parts will each have a size of 10.
# The final part will contain the remaining 3 elements.
# Examples:
# Array: [1, 2, 3]
# Chunk size: 1
# Expected solution --> [[1], [2], [3]]
#
# Array: [1, 2, 3, 4, 5]
# Chunk size: 2
# Expected solution --> [[1, 2], [3, 4], [5]]

def make_parts(arr, chunk_size):
    result = []
    counter = 0
    arrs = []
    for i in arr:
        if counter == chunk_size:
            result.append(arrs)
            arrs = [i]
            counter = 1
        else:
            arrs.append(i)
            counter += 1
    if arrs:
        result.append(arrs)
    return result