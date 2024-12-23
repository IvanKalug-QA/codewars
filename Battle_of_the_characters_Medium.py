# Groups of characters decided to make a battle. Help them to figure out what group is more powerful. Create a function that will accept 2 variables and return the one who's stronger.
#
# Rules
# Each character has its own power:
#   A = 1, B = 2, ... Y = 25, Z = 26
#   a = 0.5, b = 1, ... y = 12.5, z = 13
# Only alphabetical characters can and will participate in a battle.
# Only two groups to a fight.
# Group whose total power (a + B + c + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples
# "One", "Two"  -->  "Two"
# "ONE", "NEO"  -->  "Tie!"

from string import ascii_uppercase
def battle(x: str, y: str) -> str:
    d = {'a': 0.5, 'b': 1.0, 'c': 1.5,
        'd': 2.0, 'e': 2.5, 'f': 3.0, 'g': 3.5,
        'h': 4.0, 'i': 4.5, 'j': 5.0, 'k': 5.5, 'l': 6.0,
        'm': 6.5, 'n': 7.0, 'o': 7.5, 'p': 8.0, 'q': 8.5,
        'r': 9.0, 's': 9.5, 't': 10.0, 'u': 10.5,
        'v': 11.0, 'w': 11.5, 'x': 12.0, 'y': 12.5, 'z': 13.0}
    counter_x = 0
    counter_y = 0
    for i in x:
        if i.isupper():
            counter_x += ascii_uppercase.index(i) + 1
        else:
            counter_x += d[i]
    for i in y:
        if i.isupper():
            counter_y += ascii_uppercase.index(i) + 1
        else:
            counter_y += d[i]
    if counter_x > counter_y:
        return x
    elif counter_y > counter_x:
        return y
    return 'Tie!'