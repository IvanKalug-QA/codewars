# Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a multiple of three.
#
# Return n if the input is already a multiple of three, and if no such number exists, return null, a similar empty value, or -1.
#
# Examples
# 1      => null
# 25     => null
# 36     => 36
# 1244   => 12
# 952406 => 9

def prev_mult_of_three(n):
    if n % 3 == 0:
        return n
    elif len(str(n)) == 1 and n % 3 != 0:
        return None
    while len(str(n)) > 1 and n % 3 != 0:
        n = int(str(n)[0:-1])
    return n if n % 3 == 0 else None