# Task:
# Based on the received dimensions, a and b, of an ellipse, calculare its area and perimeter.
#
# Example:
# Input: ellipse(5,2)
#
# Output: "Area: 31.4, perimeter: 23.1"
# Note: The perimeter approximation formula you should use: π * (3/2(a+b) - sqrt(ab))
#
# Have fun :)

from math import sqrt, pi
def ellipse(a, b):
    perimetr = pi * ((3 / 2) * (a + b) - sqrt(a * b))
    area = pi * a * b
    return f'Area: {round(area, 1)}, perimeter: {round(perimetr, 1)}'