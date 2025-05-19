# A triangle is called an equable triangle if its area equals its perimeter. Return true, if it is an equable triangle, else return false. You will be provided with the length of sides of the triangle. Happy Coding!

import math
def equable_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    res = (a + b + c) // 2
    return math.sqrt(res * (res - a) * (res - b) * (res - c)) == a + b + c