# iven an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
#
# Examples:
#
# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).
#
# You can assume that all inputs are valid integers.

def round_to_next5(n):
    if n == -1:
        return 0
    if n >= 0:
        for i in range(n, n + 10):
            if i % 5 == 0:
                return i
    for i in range(n, abs(n) + 10):
        if abs(i) % 5 == 0:
            return i