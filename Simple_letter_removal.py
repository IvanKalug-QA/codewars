# In this Kata, you will be given a lower case string and your task will be to remove k characters from that string using the following rule:
#
# - first remove all letter 'a', followed by letter 'b', then 'c', etc...
# - remove the leftmost character first.
# For example:
# solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
# solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
# solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b'
# solve('abracadabra', 8) = 'rdr'
# solve('abracadabra',50) = ''
# More examples in the test cases. Good luck!

from string import ascii_lowercase
def solve(st,k):
    result = [i for i in st]
    for i in ascii_lowercase:
        for j in range(len(result)):
            if k == 0:
                return ''.join(result)
            elif result[j] == i:
                result[j] = ''
                k -= 1
    return ''.join(result)