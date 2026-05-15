# Kata Task
# You are given a list of cogs in a gear train, and an index n for the nth cog in the list.

# Each element represents the number of teeth of that cog

# e.g. [100, 50, 25] means

# 1st cog has 100 teeth
# 2nd cog has 50 teeth
# 3rd cog has 25 teeth
# If the nth cog rotates clockwise at 1 RPM what is the RPM of the cogs at each end of the gear train?

# Notes

# no two cogs share the same shaft
# return an array whose two elements are RPM of the first and last cogs respectively
# use negative numbers for anti-clockwise rotation
# for convenience n is zero-based
# For C and NASM coders, the returned array will be free'd.

def cog_RPM(cogs, n):
    sign_first = -1 if n % 2 == 1 else 1
    rpm_first = sign_first * (cogs[n] / cogs[0])
    last_idx = len(cogs) - 1
    distance_to_last = last_idx - n
    sign_last = -1 if distance_to_last % 2 == 1 else 1
    rpm_last = sign_last * (cogs[n] / cogs[last_idx])
    return [rpm_first, rpm_last]