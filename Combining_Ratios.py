# 2 ratios given as strings in the form A:B and B:C

# eg 12:4 3:7

# Your program must return the ratio of A:B:C in simplest form

# eg 12:4 3:7 ---> 9:3:7

# Given Ratios are not in simplest form A,B and C are always in the range of 1 --> 1e5

# return as a string in the format "9:3:7"

def merge_ratios(ratio1,ratio2):
    a1, b1 = map(int, ratio1.split(':'))
    a2, b2 = map(int, ratio2.split(':'))
    
    lcm_b = abs(b1 * a2) // __import__('math').gcd(b1, a2)
    factor1 = lcm_b // b1
    factor2 = lcm_b // a2
    
    A = a1 * factor1
    B = lcm_b
    C = b2 * factor2
    
    gcd_all = __import__('math').gcd(__import__('math').gcd(A, B), C)
    return f"{A//gcd_all}:{B//gcd_all}:{C//gcd_all}"