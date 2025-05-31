# You are given an array with several "even" words, one "odd" word, and some numbers mixed in.
#
# Determine if any of the numbers in the array is the index of the "odd" word. If so, return true, otherwise false.

def odd_ball(arr):
    for i in arr:
        if isinstance(i, int):
            if i < len(arr) and arr[i] == 'odd':
                return True
    return False