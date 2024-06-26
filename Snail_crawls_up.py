# The snail crawls up the column. During the day it crawls up some distance. During the night she sleeps, so she slides down for some distance (less than crawls up during the day).
#
# Your function takes three arguments:
#
# The height of the column (meters)
# The distance that the snail crawls during the day (meters)
# The distance that the snail slides down during the night (meters)
# Calculate number of day when the snail will reach the top of the column.

def snail(column, day, night):
    snail = 0
    count = 0
    for i in range(100):
        snail += day
        count += 1
        if snail >= column:
            return count
        else:
            snail -= night