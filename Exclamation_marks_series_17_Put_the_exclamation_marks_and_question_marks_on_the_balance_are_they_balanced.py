# Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?
#
# If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".
#
# Examples
# "!!", "??"     -->  "Right"
# "!??", "?!!"   -->  "Left"
# "!?!!", "?!?"  -->  "Left"
# "!!???!????", "??!!?!!!!!!!"  -->  "Balance"

def balance(left, right):
    w = (left.count('!') * 2) + (left.count('?') * 3)
    w1 = (right.count('!') * 2) + (right.count('?') * 3)
    if w > w1:
        return 'Left'
    elif w1 > w:
        return 'Right'
    else:
        return 'Balance'