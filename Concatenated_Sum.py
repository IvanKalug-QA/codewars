# The number 198 has the property that 198 = 11 + 99 + 88, i.e., if each of its digits is concatenated twice and then summed, the result will be the original number. It turns out that 198 is the only number with this property. However, the property can be generalized so that each digit is concatenated n times and then summed.
#
# Examples
# original number =2997 , n=3
# 2997 = 222+999+999+777 and here each digit is concatenated three times.
#
# original number=-2997 , n=3
#
# -2997 = -222-999-999-777 and here each digit is concatenated three times.
# Task
# Write a function named check_concatenated_sum that tests if a number has this generalized property.

def check_concatenated_sum(n, t):
    if t == 0:
        return False
    l = list()
    start = n
    flag = False
    if n < 0:
        flag = True
    if flag:
        n = str(n)[1::]
    else:
        n = str(n)
    for i in n:
        l.append(int(i*t))
    if flag:
        if len(l) == 1:
            return True
        return -int(sum(l)) == start
    return sum(l) == start