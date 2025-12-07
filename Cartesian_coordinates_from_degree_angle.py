# Write a simple function that takes polar coordinates (an angle in degrees and a radius) and returns the equivalent cartesian coordinates.

# For example:

# coordinates(90,1)
# => (0.0, 1.0)

# coordinates(45, 1)
# => (0.7071067812, 0.7071067812)

import math
def coordinates(degrees: float, radius: float) -> tuple[float, float]:
    radians = math.radians(degrees)
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    return (round(x, 10), round(y, 10))