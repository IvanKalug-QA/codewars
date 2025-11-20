# Your job is to fix the parentheses so that all opening and closing parentheses (brackets) have matching counterparts. You will do this by appending parenthesis to the beginning or end of the string. The result should be of minimum length. Don't add unnecessary parenthesis.

# The input will be a string of varying length, only containing '(' and/or ')'.

# For example:

# Input: ")("
# Output: "()()"

# Input: "))))(()("
# Output: "(((())))(()())"

def fix_parentheses(strng):
    balance = 0
    need_open = 0
    
    for ch in strng:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        if balance < 0:
            need_open += 1
            balance = 0
    
    need_close = balance
    
    return '(' * need_open + strng + ')' * need_close