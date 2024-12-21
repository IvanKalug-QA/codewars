# Description:
# Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 strings and return the one who's stronger.
#
# Rules:
# Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
# Strings will consist of uppercase letters only
# Only two groups to a fight.
# Group whose total power (A + B + C + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples:
#       * "ONE", "TWO"  -> "TWO"`
#       * "ONE", "NEO"  -> "Tie!"

from string import ascii_uppercase
def battle(x, y):
    x_counter = 0
    y_counter = 0
    for word in x:
        x_counter += ascii_uppercase.index(word) + 1
    for word in y:
        y_counter += ascii_uppercase.index(word) + 1
    if x_counter > y_counter:
        return x
    elif y_counter > x_counter:
        return y
    return 'Tie!'