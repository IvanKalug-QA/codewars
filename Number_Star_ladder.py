# Using n as a parameter in the function pattern, where n > 0, complete the code to get the pattern:
#
# 1
# 1*2
# 1**3
# 1***4
# ... and so on...
# Note: There is no newline in the end (after the pattern ends).
#
# Examples
# pattern(3) should return "1\n1*2\n1**3", e.g. the following:
#
# 1
# 1*2
# 1**3
# pattern(10): should return the following:
#
# 1
# 1*2
# 1**3
# 1***4
# 1****5
# 1*****6
# 1******7
# 1*******8
# 1********9
# 1*********10

def pattern(n):
    if n == 1:
        return str(1)
    result = [str(1)]
    id = 2
    counter = 1
    for i in range(2, n + 1):
        result.append(str(1) + ('*' * counter) + str(id))
        id += 1
        counter += 1
    return '\n'.join(result)