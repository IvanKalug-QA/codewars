# Background
# I have stacked some cannon balls in a triangle-based pyramid.

# Like this,

# cannon balls triangle base
# Kata Task
# Given the number of layers of my stack, what is the total height?

# Return the height as multiple of the ball diameter.

# Example
# The image above shows a stack of 3 layers.

# Notes
# layers >= 0
# approximate answers (within 0.001) are good enough

import math

def stack_height_3d(layers):
    if layers == 0:
        return 0.0
    if layers == 1:
        return 1.0
    return 1 + (layers - 1) * math.sqrt(2/3)