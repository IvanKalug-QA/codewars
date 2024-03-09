# Given a string, turn each character into its ASCII character code and join them together to create a number - let's call this number total1:
#
# 'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
# Then replace any incidence of the number 7 with the number 1, and call this number 'total2':
#
# total1 = 656667
#               ^
# total2 = 656661
#               ^
# Then return the difference between the sum of the digits in total1 and total2:
#
#   (6 + 5 + 6 + 6 + 6 + 7)
# - (6 + 5 + 6 + 6 + 6 + 1)
# -------------------------
#                        6

def calc(x):
    s = ''
    for i in x:
        s += str(ord(i))
    d = s
    for i in d:
        if i == "7":
            d = d.replace("7", "1")
    r = str(int(s) - int(d))
    c = 0
    for i in r:
        if i != '0':
            c += int(i)
    return c