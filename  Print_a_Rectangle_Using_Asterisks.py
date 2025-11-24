# Write a method that, given two arguments, width and height, returns a string representing a rectangle with those dimensions.

# The rectangle should be filled with spaces, and its borders should be composed of asterisks (*).

# For example, given width = 3 and height = 3:

# ***
# * *
# ***
# End each line of the string (including the last one) with a carriage return-line feed combination.

# Note: You may assume that width and height will always be greater than zero.

def get_rectangle_string(width, height):
    result = []
    
    for i in range(height):
        if i == 0 or i == height - 1:
            result.append('*' * width)
        else:
            if width == 1:
                result.append('*')
            else:
                result.append('*' + ' ' * (width - 2) + '*')
    
    return '\r\n'.join(result) + '\r\n'