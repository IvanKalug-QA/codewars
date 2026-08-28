# Create a function to determine whether or not two circles are colliding. You will be given the position of both circles in addition to their radii:

# def collision(x1, y1, radius1, x2, y2, radius2):  
#   # collision?
# If a collision is detected, return true. If not, return false.

def collision(x1, y1, radius1, x2, y2, radius2):
    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    radius_sum = radius1 + radius2
    
    return distance_squared <= radius_sum ** 2