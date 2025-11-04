# Extend the Math object/module to convert degrees to radians and vice versa. Return the result in string format, rounded to two decimal points when not an integer, otherwise truncate the result (see the examples).

# Note that all methods of Math object are static.

# Examples
# math.degrees(math.pi)  -->  "180deg"
# math.radians(180)      -->  "3.14rad"

# math module is already imported
# default degrees and radians methods disabled

def degrees(rad):
    degrees_val = rad * 180 / math.pi
    
    if degrees_val.is_integer():
        return f"{int(degrees_val)}deg"
    else:
        rounded = round(degrees_val, 2)
        if rounded == int(rounded):
            return f"{int(rounded)}deg"
        else:
            return f"{rounded:.10f}".rstrip('0').rstrip('.') + "deg"

def radians(deg):
    radians_val = deg * math.pi / 180
    
    if radians_val.is_integer():
        return f"{int(radians_val)}rad"
    else:
        rounded = round(radians_val, 2)
        if rounded == int(rounded):
            return f"{int(rounded)}rad"
        else:
            return f"{rounded:.10f}".rstrip('0').rstrip('.') + "rad"

math.degrees = degrees
math.radians = radians