# This is a follow up from my kata Insert Dashes.

# Write a function that takes a non-negative integer, insert dashes ('-') between each two odd digits and insert asterisks ('*') between each two nonzero even digits.

# For example:

# 454793 --> "4547-9-3"
# 1012356895 --> "10123-56*89-5"
# Note: Digit zero ('0') is not considered when inserting dashes or asterisks.

def insert_dash2(num):
    digits = str(num)
    result = digits[0]
    
    for i in range(1, len(digits)):
        current = int(digits[i])
        previous = int(digits[i-1])
        
        if previous % 2 == 1 and current % 2 == 1:
            result += '-' + digits[i]
        elif previous != 0 and current != 0 and previous % 2 == 0 and current % 2 == 0:
            result += '*' + digits[i]
        else:
            result += digits[i]
    
    return result