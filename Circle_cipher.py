# Imagine a circle. To encode the word codewars, we could split the circle into 8 parts (as codewars has 8 letters):

# Then add the letters in a clockwise direction:Then remove the circle:
# If we read the result from left to right, we get csordaew.

# Decoding is the same process in reverse. If we decode csordaew, we get codewars.

# Examples:
# encode "codewars" -> "csordaew"
# decode "csordaew" -> "codewars"
# encode "white" -> "wehti"
# decode "wehti" -> "white"

def encode(s: str) -> str:
    result = []
    left, right = 0, len(s) - 1
    
    while left <= right:
        if left == right:
            result.append(s[left])
            break
        result.append(s[left])
        result.append(s[right])
        left += 1
        right -= 1
    
    return ''.join(result)


def decode(s: str) -> str:
    result = [''] * len(s)
    left, right = 0, len(s) - 1
    pos = 0
    
    while left <= right:
        if left == right:
            result[left] = s[pos]
            break
        result[left] = s[pos]
        result[right] = s[pos + 1]
        left += 1
        right -= 1
        pos += 2
    
    return ''.join(result)