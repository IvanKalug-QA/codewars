# Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), false otherwise.

def is_letter(s):
    if len(s) >= 2:
        return False
    for i in s:
        if i.isalpha():
            return True
    return False