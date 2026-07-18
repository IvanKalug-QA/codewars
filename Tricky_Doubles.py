# Write a function that returns twice the input value, unless the value is a "tricky double."

# A number is considered a tricky double if it consists of two identical halves with no extra digits. For example, 44, 1212, and 7777 are tricky doubles because each half of the number is the same (4 and 4, 12 and 12, 77 and 77).

# If the input value is a tricky double, return it as-is. Otherwise, return the value multiplied by 2.

# Examples of tricky double numbers:

# 44 - consists of two 4s
# 77 - consists of two 7s
# 3333 - consists of two 33s
# 8787 - consists of two 87s
# 100100 - consists of two 100s
# In the example 8787, the number 87 is doubled (appears twice).

# trickyDoubles(15)   // should return 30
# trickyDoubles(100)  // should return 200
# trickyDoubles(4343) // should return 4343


def tricky_doubles(num):
    num_str = str(num)
    length = len(num_str)
    
    if length % 2 != 0:
        return num * 2
    
    half = length // 2
    first_half = num_str[:half]
    second_half = num_str[half:]
    
    if first_half == second_half:
        return num
    else:
        return num * 2