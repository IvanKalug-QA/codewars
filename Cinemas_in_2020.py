# Given an array of seats, return the maximum number of new people which can be seated, as long as there is at least a gap of 2 seats between people.
#
# Empty seats are given as 0.
# Occupied seats are given as 1.
# Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.
# Examples
# [0, 0, 0, 1, 0, 0, 1, 0, 0, 0] ➞ 2
# // [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
#
# [0, 0, 0, 0] ➞ 2
# // [1, 0, 0, 1]
#
# [1, 0, 0, 0, 0, 1] ➞ 0
# // There is no way to have a gap of at least 2 chairs when adding someone else.
# Notes
# Notice how there may be several possibilities for assigning seats to people, but these cases won't affect the results.
# All seats will be valid.

def maximum_seating(lst):
    n = len(lst)
    count = 0
    i = 0
    while i < n:
        if lst[i] == 0:
            left_clear = (i - 1 < 0 or lst[i - 1] == 0) and (i - 2 < 0 or lst[i - 2] == 0)
            right_clear = (i + 1 >= n or lst[i + 1] == 0) and (i + 2 >= n or lst[i + 2] == 0)

            if left_clear and right_clear:
                count += 1
                lst[i] = 1
                i += 2
                continue
        i += 1
    return count