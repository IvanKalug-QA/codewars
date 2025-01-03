# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
#
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
#
# Examples
#  123 ->  321
# -456 -> -654
# 1000 ->    1

def reverse_number(n):
    if len(str(n)) == 1:
        return n
    numb = ''
    min = ''
    if '-' in str(n):
        numb = str(n)[1:][::-1]
        min = '-'
    else:
        numb = str(n)[::-1]
    numb = min + str(int(numb))
    return int(numb)