# You have two arrays in this kata, every array contains unique elements only. Your task is to calculate number of elements in the first array which are also present in the second array.

def match_arrays(v, r):
    count = 0
    for i in r:
        if i in v:
            count += 1
    return count