# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x, y attributes. Circle objects have center which is a Point, and radius which is a number.

# Write a function calculating distance between Circle a and Circle b.

# If they're overlapping or one is completely within the other, just return zero.

# Tests round answers to 6 decimal places, so you don't need to round them yourselves.

import math

def distance_between_circles(a, b):
    dx = a.center.x - b.center.x
    dy = a.center.y - b.center.y
    d = math.hypot(dx, dy)  # sqrt(dx*dx + dy*dy)
    if d <= a.radius + b.radius or d <= abs(a.radius - b.radius):
        return 0.0
    return d - a.radius - b.radius