# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

def strip_comments(strng, markers):
    l = strng.split('\n')
    res = []
    for i in l:
        result = []
        for j in i:
            if j in markers:
                break
            else:
                result.append(j)
        res.append(''.join(result).rstrip())
    return '\n'.join(res)