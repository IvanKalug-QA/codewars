# In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.
#
# For example:
#
# solve("our code") = "edo cruo"
# -- Normal reversal without spaces is "edocruo".
# -- However, there is a space at index 3, so the string becomes "edo cruo"
#
# solve("your code rocks") = "skco redo cruoy".
# solve("codewars") = "srawedoc"
# More examples in the test cases. All input will be lower case letters and in some cases spaces.
#
# Good luck!

def solve(s):
    result =[i for i in s]
    l = 0
    r = len(result) - 1
    while l <= r:
        if result[l] == ' ':
            l += 1
        elif result[r] == ' ':
            r -= 1
        else:
            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1
    return ''.join(result)