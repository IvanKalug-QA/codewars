# There is a naughty number hidden somewhere in the list. Find the index of it, if you are strong enough, of course!

# Input:
# You will receive an array of arrays (a list of lists).
# Each sub-array can only contain either another array or a single number.
# There will always be at least one sub-array in the input.
# There will be only one number hidden in the sub-arrays
# Output:
# Return the index of the first-level sub-array that contains the hidden number.

# Examples:
# [ [[[]]] , [[]], [], [], [[2]] ] -> index is 4

# [ [1] ] -> index is 0

# [ [], [8], [] , [] ] -> index is 1

def naughty_number(arr):
    for i, sub in enumerate(arr):
        if isinstance(sub, list):
            flat = str(sub).replace("[", "").replace("]", "").strip()
            if flat and flat.isdigit():
                return i
    return -1