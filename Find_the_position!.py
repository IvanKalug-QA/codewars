# DESCRIPTION:
# When provided with a letter, return its position in the alphabet.
#
# Input :: "a"
#
# Ouput :: "Position of alphabet: 1"

def position(a):
    return 'Position of alphabet: ' + str('abcdefghijklmnopqrstuvwxyz'.index(a) + 1)