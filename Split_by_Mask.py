# Given a string and a mask (a list of lengths), split the string into its parts accordingly.

# Examples:
# |     String      |  Mask (lengths)  |          Output           |
# |-----------------|------------------|---------------------------|
# |  "1234567890"   |  (3, 3, 4)       |  ["123", "456", "7890"]   |
# |  "codewars"     |  (4, 4)          |  ["code", "wars"]         |
# Notes:
# The mask only contains strictly positive integers.
# A mask is valid if and only if the sum of the lengths is equal to the length of the string.
# Otherwise, return None, Nothing or a similar empty value.

def split_by_mask(strng, mask):
    if sum(mask) != len(strng):
        return None
    
    result = []
    start = 0
    for length in mask:
        result.append(strng[start:start + length])
        start += length
    
    return result