# DESCRIPTION:
# For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input.
# Duplicate numbers within the array are possible.
#
# Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc).
# Write a function where you will win the game if your numbers can spell "BINGO".
# They do not need to be in the right order in the input array. Otherwise you will lose.
# Your outputs should be "WIN" or "LOSE" respectively.

def bingo(array):
    tuple = {2:'B', 9:'I', 14:'N', 7:'G', 15:'O'}
    l = []
    for i in array:
        if i == 2:
            l.append(i)
        if i == 9:
            l.append(i)
        if i == 14:
            l.append(i)
        if i == 7:
            l.append(i)
        if i == 15:
            l.append(i)
    lis = list(set(l))
    if len(lis) < 5:
        return 'LOSE'
    return 'WIN'