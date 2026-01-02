# Given a number n, define its scORe to be 0 | 1 | 2 | 3 | .. | n, where | is the bitwise OR operator.

# Write a function that takes n and finds its scORe.

#         n |   scORe n
# ----------|----------
#         0 |         0
#         1 |         1
#        49 |        63
# 1 000 000 | 1 048 575

def score(n):
    if n == 0:
        return 0
    
    msb_position = n.bit_length()
    
    return (1 << msb_position) - 1