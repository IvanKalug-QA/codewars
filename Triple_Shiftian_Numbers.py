# Much cooler than your run-of-the-mill Fibonacci numbers, the Triple Shiftian are so defined: T[n] = 4 * T[n-1] - 5 * T[n-2] + 3 * T[n-3].

# You are asked to create a function which accept a base with the first 3 numbers and then returns the nth element.

# Given base=[1,1,1], n=25 ==> 1219856746
# Given base=[1,2,3], n=25 ==> 2052198929
# Given base=[6,7,2], n=25 ==> -2575238999
# Given base=[3,2,1], n=35 ==> 23471258855679
# Given base=[1,9,2], n=2  ==> 2
# Note: this is meant to be an interview quiz, so the description is scarce in detail on purpose

def triple_shiftian(base, n):
    if n == 0:
        return base[0]
    if n == 1:
        return base[1]
    if n == 2:
        return base[2]
    
    t0, t1, t2 = base[0], base[1], base[2]
    for i in range(3, n + 1):
        t_next = 4 * t2 - 5 * t1 + 3 * t0
        t0, t1, t2 = t1, t2, t_next
    return t2