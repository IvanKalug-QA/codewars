# In this Kata, you will be given a string and your task is to return the most valuable character. The value of a character is the difference between the index of its last occurrence and the index of its first occurrence. Return the character that has the highest value. If there is a tie, return the alphabetically lowest character. [For Golang return rune]
#
# All inputs will be lower case.
#
# For example:
# solve('a') = 'a'
# solve('ab') = 'a'. Last occurrence is equal to first occurrence of each character. Return lexicographically lowest.
# solve("axyzxyz") = 'x'
# More examples in test cases. Good luck!

def solve(st):
    result = [-1] * 27
    counter = {}
    for i in range(len(st)):
        if st[i] in counter:
            result[ord(st[i]) - 97] = i - counter[st[i]]
        else:
            counter[st[i]] = i
            result[ord(st[i]) - 97] = 0
    res = -1
    word = ''
    for i in range(len(result)):
        if result[i] > res:
            res = result[i]
            word = chr(i + 97)
    return word