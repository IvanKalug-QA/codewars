# Steps
#
# Square the numbers that are greater than zero.
# Multiply by 3 every third number.
# Multiply by -1 every fifth number.
# Return the sum of the sequence.
# Example
# { -2, -1, 0, 1, 2 } returns -6
#
# 1. { -2, -1, 0, 1 * 1, 2 * 2 }
# 2. { -2, -1, 0 * 3, 1, 4 }
# 3. { -2, -1, 0, 1, -1 * 4 }
# 4. -6

def calc(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] **= 2
    for i in range(2, len(arr), 3):
        arr[i] *= 3
    for i in range(4, len(arr), 5):
        arr[i] //= -1
    return sum(arr)