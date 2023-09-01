# DESCRIPTION:
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    c1 = 0
    c2 = 2
    l = []
    count = 0
    while count < len(s):
        if len(s) == 0:
            break
        if len(s[c1:c2]) % 2  == 0:
            l.append(s[c1:c2])
            c1 += 2
            c2 += 2
            count += 2
        if len(s[c1:c2]) % 2 != 0:
            l.append(s[c1:c2] + '_')
            c1 += 2
            c2 += 2
            count += 1
    return l