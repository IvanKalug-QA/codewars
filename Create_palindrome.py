# Consider the string "adfa" and the following rules:

# a) each character MUST be changed either to the one before or the one after in alphabet. 
# b) "a" can only be changed to "b" and "z" to "y". 
# From our string, we get:

# "adfa" -> ["begb","beeb","bcgb","bceb"]

# Here is another example: 
# "bd" -> ["ae","ac","ce","cc"]

# --We see that in each example, one of the outcomes is a palindrome. That is, "beeb" and "cc".
# You will be given a lowercase string and your task is to return True if at least one of the outcomes is a palindrome or False otherwise.

# More examples in test cases. Good luck!

def solve(st):
    n = len(st)
    
    for i in range(n // 2):
        left = st[i]
        right = st[n - 1 - i]
        
        left_options = set()
        if left == 'a':
            left_options.add('b')
        elif left == 'z':
            left_options.add('y')
        else:
            left_options.add(chr(ord(left) - 1))
            left_options.add(chr(ord(left) + 1))
        
        right_options = set()
        if right == 'a':
            right_options.add('b')
        elif right == 'z':
            right_options.add('y')
        else:
            right_options.add(chr(ord(right) - 1))
            right_options.add(chr(ord(right) + 1))
        
        if not (left_options & right_options):
            return False
    
    return True