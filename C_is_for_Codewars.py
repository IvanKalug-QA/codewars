# Task:
# Build a string representing a capital letter C of a given size out of 'C' characters.

# Examples:
# generate_C(1) 
# should return this string:

# CCCCC
# C
# C
# C
# CCCCC
# generate_C(2) 
# should be

# CCCCCCCCCC
# CCCCCCCCCC
# CC
# CC
# CC
# CC
# CC
# CC
# CCCCCCCCCC
# CCCCCCCCCC
# and so on. Given size, the string should have 5*size lines, following the format above. size is a positive integer ≤ 2000.

# Note that extra spaces after the C's in any line are incorrect. And the last line should not terminate with "\n".

# This kata was inspired by A for Apple, but takes a different approach to generating letters.

def generate_C(size):
    top_bottom = 'C' * (5 * size)
    middle = 'C' * size

    lines = (
        [top_bottom] * size +
        [middle] * (3 * size) +
        [top_bottom] * size
    )

    return '\n'.join(lines)