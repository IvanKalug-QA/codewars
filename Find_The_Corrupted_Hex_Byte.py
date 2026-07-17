# Task
# A hexadecimal dump should contain only valid hexadecimal bytes.

# A valid byte:

# consists of exactly two characters.
# contains only hexadecimal digits (0-9, A-F).
# uses uppercase letters only.
# Return the index of the first corrupted byte.

# If every byte is valid, return -1.

# Examples
# find_corrupted_byte(["48", "65", "6C", "6C", "6F"])

# -1
# find_corrupted_byte(["48", "65", "6G", "6C", "6F"])

# 2
# find_corrupted_byte(["48", "6", "6C"])

# 1
# find_corrupted_byte(["48", "6c", "6F"])

# 1
# Notes
# The input is a list of strings.
# An empty list is considered valid.

HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for i, byte in enumerate(dump):
        if len(byte) != 2:
            return i
        if byte[0] not in HEX or byte[1] not in HEX:
            return i
    return -1