# A squared string is a string of n lines, each substring being n characters long. We are given two n-squared strings.

# For example:

# s1 = "abcd\nefgh\nijkl\nmnop"

# s2 = "qrst\nuvwx\nyz12\n3456"

# Let us build a new string strng of size (n + 1) x n in the following way:

# The first line of strng has the first char of the first line of s1 plus the chars of the last line of s2.
# The second line of strng has the first two chars of the second line of s1 plus the chars of the penultimate line of s2 except the last char
# and so on until the nth line of strng has the n chars of the nth line of s1 plus the first char of the first line of s2.
# So we have:

# strng --> "a3456\nefyz1\nijkuv\nmnopq"

# or printed:
# abcd    qrst  -->  a3456
# efgh    uvwx       efyz1
# ijkl    yz12       ijkuv
# mnop    3456       mnopq

def compose(s1, s2):
    lines1 = s1.split('\n')
    lines2 = s2.split('\n')
    n = len(lines1)
    
    result = []
    
    for i in range(n):
        first_part = lines1[i][:i+1]
        second_part = lines2[n-1-i][:n-i]
        result.append(first_part + second_part)
    
    return '\n'.join(result)