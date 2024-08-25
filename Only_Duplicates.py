# Given a string, remove any characters that are unique from the string.
#
# Example:
#
# input: "abccdefee"
#
# output: "cceee"

def only_duplicates(st):
    res = ''
    for i in st:
        if st.count(i) > 1:
            res += i
    return res