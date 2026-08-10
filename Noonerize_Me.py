# Spoonerize... with numbers... numberize?... numboonerize?... noonerize? ...anyway! If you don't yet know what a spoonerism is and haven't yet tried my spoonerism kata, please do check it out first.

# You will create a function which takes an array of two positive integers, spoonerizes them, and returns the positive difference between them as a single number or 0 if the numbers are equal:

# [123, 456] = 423 - 156 = 267
# Your code must test that all array items are numbers and return "invalid array" if it finds that either item is not a number. The provided array will always contain 2 elements.

# When the inputs are valid, they will always be integers, no floats will be passed. However, you must take into account that the numbers will be of varying magnitude, between and within test cases.

def noonerize(numbers):
    if not all(isinstance(num, int) for num in numbers):
        return "invalid array"
    num1 = str(numbers[0])
    num2 = str(numbers[1])
    swapped1 = num2[0] + num1[1:] if len(num1) > 1 else num2[0]
    swapped2 = num1[0] + num2[1:] if len(num2) > 1 else num1[0]
    new_num1 = int(swapped1)
    new_num2 = int(swapped2)
    
    return abs(new_num1 - new_num2)