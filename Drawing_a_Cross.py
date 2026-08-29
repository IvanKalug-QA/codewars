# The aim of this kata is to write function drawACross / draw_a_cross which returns a cross shape with 'x' characters on a square grid of size and height of our sole input n. All non-'x' characters in the grid should be filled with a space character (" ").

# For example for drawACross(7) / draw_a_cross(7), the function should draw the following grid:

# x     x
#  x   x 
#   x x  
#    x   
#   x x  
#  x   x 
# x     x
# The arms of the cross must only intersect through one central 'x' character, and start in the corner of the grid, so for even values of n, return "Centered cross not possible!"

# If n<3, function should return "Not possible to draw cross for grids less than 3x3!"

def draw_a_cross(n):
    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"
    if n % 2 == 0:
        return "Centered cross not possible!"
    
    result = []
    for i in range(n):
        row = [' '] * n
        row[i] = 'x'
        row[n - 1 - i] = 'x'
        result.append(''.join(row))
    
    return '\n'.join(result)