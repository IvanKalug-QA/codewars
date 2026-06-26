# Maxie is the largest number that can be obtained by swapping two digits of an integer, Minnie is the smallest number. Create a function that takes an integer and returns Maxie and Minnie. Leading zeroes are not permitted. All test cases are positive integers of three digits or more. Sometimes no swaps are needed.

# Examples:
# swap(12340) → (42310,10342)
# swap(98761) → (98761,18769)>>No swap needed for Maxie.
# swap(9000) → (9000,9000)>>No swaps allowed.
# swap(90888) → (98880,80889)

def swap(number):
    digits = list(str(number))
    n = len(digits)
    
    max_digits = digits.copy()
    for i in range(n):
        for j in range(i + 1, n):
            max_digits[i], max_digits[j] = max_digits[j], max_digits[i]
            if max_digits[0] != '0':
                current = int(''.join(max_digits))
                best = int(''.join(digits))
                if current > best:
                    digits = max_digits.copy()
                    best = current
            max_digits[i], max_digits[j] = max_digits[j], max_digits[i]
    
    maxie = int(''.join(digits))
    
    digits = list(str(number))
    
    min_digits = digits.copy()
    best = int(''.join(digits))
    
    for i in range(n):
        for j in range(i + 1, n):
            min_digits[i], min_digits[j] = min_digits[j], min_digits[i]
            if min_digits[0] != '0':
                current = int(''.join(min_digits))
                if current < best:
                    digits = min_digits.copy()
                    best = current
            min_digits[i], min_digits[j] = min_digits[j], min_digits[i]
    
    minnie = int(''.join(digits))
    
    return (maxie, minnie)