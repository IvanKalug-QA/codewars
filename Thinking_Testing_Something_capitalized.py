# DESCRIPTION:
# No Story
#
# No Description
#
# Only by Thinking and Testing
#
# Look at result of testcase, guess the code!

def testit(s):
    ans = []
    for i in s.split():
        ans.append(i[:-1] + i[-1].upper())
    return ' '.join(ans)