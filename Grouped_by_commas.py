# Finish the solution so that it takes an input n (integer) and returns a string that is the decimal representation of the number grouped by commas after every 3 digits.
#
# Assume: 0 <= n <= 2147483647
#
# Examples
#        1  ->           "1"
#       10  ->          "10"
#      100  ->         "100"
#     1000  ->       "1,000"
#    10000  ->      "10,000"
#   100000  ->     "100,000"
#  1000000  ->   "1,000,000"
# 35235235  ->  "35,235,235"

def group_by_commas(n):
    n = str(n)
    counter = 0
    res = []
    st = ''
    for i in range(len(n) - 1, -1, -1):
        if counter == 3:
            res.append(st)
            counter = 1
            st = n[i]
        else:
            st += n[i]
            counter += 1
    res.append(st)
    return ','.join(i[::-1] for i in res[::-1])