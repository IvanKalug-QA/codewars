# Write a function that returns the count of characters that have to be removed in order to get a string with no consecutive repeats.
#
# Note: This includes any characters
#
# Examples
# 'abbbbc'  => 'abc'    #  answer: 3
# 'abbcca'  => 'abca'   #  answer: 2
# 'ab cca'  => 'ab ca'  #  answer: 1

def count_repeats(txt):
    count = 0
    r = 0
    l = 0
    res = 0
    while r < len(txt):
        if txt[l] == txt[r]:
            res += 1
            r += 1
        else:
            count += res - 1
            l = r
            res = 0
    return count + (res - 1)