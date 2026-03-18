# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x, y, and z attributes. For Haskell there are Point data types described with record syntax with fields x, y, and z.

# Write a function calculating distance between Point a and Point b.


from preloaded import Point
import math

def distance_between_points(a: Point, b: Point) -> float:
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)
