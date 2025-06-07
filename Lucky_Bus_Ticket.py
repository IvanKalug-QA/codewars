# In Russia regular bus tickets usually consist of 6 digits. The ticket is called lucky when the sum of the first three digits equals to the sum of the last three digits. Write a function to find out whether the ticket is lucky or not. Return true if so, otherwise return false. Consider that input is always a string. Watch examples below.
#
# isLucky('123321') => 1+2+3 = 3+2+1 => true // The ticket is lucky
# isLucky('12341234') => false // Only six-digit numbers allowed :(
# isLucky('12a21a') => false // Letters are not allowed :(
# isLucky('100200') => false // :(
# isLucky('22') => false // :(
# isLucky('abcdef') => false // :(

def is_lucky(ticket):
    if len(ticket) != 6:
        return False
    r1 = 0
    r2 = 0
    for i in range(len(ticket)):
        if i > 2 and ticket[i].isdigit():
            r2 += int(ticket[i])
        elif i <= 2 and ticket[i].isdigit():
            r1 += int(ticket[i])
        else:
            return False
    return r1 == r2