# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

def tower_builder(n_floors):
    n = n_floors - 1
    frez = 1
    result = []
    for i in range(n_floors):
        if n == 0:
            result.append('*' * frez)
        else:
            result.append((' ' * n) + ('*' * frez) + (' ' * n))
        n -= 1
        frez += 2
    return result