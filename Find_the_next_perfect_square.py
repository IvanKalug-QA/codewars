# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.
#
# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square

import math
def is_perfect_square(num):
    return int(num ** 0.5) ** 2 == num
def find_next_square(sq):
    if sq == 0:
        return 1.0
    if not is_perfect_square(sq):
        return -1
    for i in range(sq + 1, sq + sq):
        if is_perfect_square(i):
            return i