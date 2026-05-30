# Implement:

# eight_bit_signed_number()
# which should return True if given object is a number representable by 8 bit signed integer (-128 to -1 or 0 to 127), False otherwise.

# It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.

import re

def signed_eight_bit_number(number):
    pattern = re.compile(r'(0|[1-9][0-9]?|1[01][0-9]|12[0-7]|-(?:[1-9][0-9]?|1[01][0-9]|12[0-7]|128))')
    return bool(pattern.fullmatch(number))