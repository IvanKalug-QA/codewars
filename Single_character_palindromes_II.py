# In this Kata, you will check if it is possible to convert a string to a palindrome by changing one character.

# For instance:

# solve ("abbx") = True, because we can convert 'x' to 'a' and get a palindrome. 
# solve ("abba") = False, because we cannot get a palindrome by changing any character. 
# solve ("abcba") = True. We can change the middle character. 
# solve ("aa") = False 
# solve ("ab") = True
# Good luck!

def solve(s):
    left, right = 0, len(s) - 1
    mismatches = 0
    
    while left < right:
        if s[left] != s[right]:
            mismatches += 1
            if mismatches > 1:
                return False
        left += 1
        right -= 1
    
    if mismatches == 0 and len(s) % 2 == 0:
        return False
    
    return True