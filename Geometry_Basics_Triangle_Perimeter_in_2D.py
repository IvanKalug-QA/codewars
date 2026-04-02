# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have x, y attributes. Triangle objects have attributes a, b, c describing their corners, each of them is a Point.

# Write a function calculating perimeter of a Triangle defined this way.

from preloaded import Point, Triangle

def triangle_perimeter(triangle: Triangle) -> float:
    a = triangle.a
    b = triangle.b
    c = triangle.c
    
    ab = ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5
    bc = ((b.x - c.x)**2 + (b.y - c.y)**2)**0.5
    ca = ((c.x - a.x)**2 + (c.y - a.y)**2)**0.5
    
    return ab + bc + ca