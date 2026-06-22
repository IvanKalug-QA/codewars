# Description
# As hex values can include letters A through to F, certain English words can be spelled out, such as CAFE, BEEF, or FACADE. This vocabulary can be extended by using numbers to represent other letters, such as 5EAF00D, or DEC0DE5.

# Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.

# Example
# Working with the string "BAG OF BEES":

# "BAG"  =  0, as it is not a valid hex value  
# "OF"   =  0F   =  15
# "BEES" =  BEE5 =  48869
# So the result is the sum of these: 48884 (0 + 15 + 48869)

# Notes
# Inputs are all uppercase and contain no punctuation
# 0 can be substituted for O
# 5 can be substituted for S

def hex_word_sum(s):
    words = s.split()
    total_sum = 0
    
    replacements = {
        'O': '0',
        'S': '5'
    }
    
    for word in words:
        converted = ''.join(replacements.get(char, char) for char in word)
        
        is_valid = True
        for char in converted:
            if not (char.isdigit() or ('A' <= char <= 'F')):
                is_valid = False
                break
        
        if is_valid:
            total_sum += int(converted, 16)
    
    return total_sum