# DESCRIPTION:
# Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n),
# of a positive integer n.
#
# For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121,
# since 111 is closer to 121, the square of 11, than 100, the square of 10.
#
# If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.
#
# Good luck :)

import math
def nearest_sq(n):
    f = int(math.sqrt(n))
    if f ** 2 == n:
        return n
    if math.sqrt(n) == f:
        ans = [f-1,f+1]
        dif = [abs(n - ans[0] ** 2), abs(n - ans[1] ** 2)]
        return ans[dif.index(min(dif))]**2
    ans = [f,f+1]
    dif = [abs(n - ans[0] ** 2), abs(n - ans[1] ** 2)]
    return ans[dif.index(min(dif))]**2