# You should write a simple function that takes string as input and checks if it is a valid Russian postal code, returning true or false.
#
# A valid postcode should be 6 digits with no white spaces, letters or other symbols. Empty string should also return false.
#
# Please also keep in mind that a valid post code cannot start with 0, 5, 7, 8 or 9
#
# Examples
# Valid postcodes:
#
# 198328
# 310003
# 424000
# Invalid postcodes:
#
# 056879
# 12A483
# 1@63
# 111

def zipvalidate(postcode):
    if len(postcode) < 6 or len(postcode) > 6:
        return False
    count = 0
    for i in postcode:
        if i.isdigit():
            count += 1
    if count == len(postcode):
        if postcode[0] == '0' or postcode[0] == '5' or postcode[0] == '7' or postcode[0] == '8' or postcode[0] == '9':
            return False
        return True
    return False