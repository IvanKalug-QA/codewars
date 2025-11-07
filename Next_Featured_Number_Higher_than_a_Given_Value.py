# Make a function that receives a value, and outputs the smallest higher number than the given value, and this number belong to a set of positive integers that have the following properties:

# their digits occur only once

# they are odd

# they are multiple of three

# next_numb(12) == 15

# next_numb(13) == 15

# next_numb(99) == 105

# next_numb(999999) == 1023459

# next_number(9999999999) == "There is no possible number that fulfills those requirements"
# Enjoy the kata!!

def next_numb(val):
    val += 1
    max_limit = 9876543210
    
    while val <= max_limit:
        s = str(val)
        if len(s) == len(set(s)) and val % 2 != 0 and val % 3 == 0:
            return val
        val += 1
    
    return "There is no possible number that fulfills those requirements"