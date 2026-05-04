# Given a time in a time format class, return it without year, month and day.

# It should return a string including milliseconds with 3 decimals.

# Example:

# datetime(2016, 2, 8, 16, 42, 59)
# #Should return: 
# "16:42:59,000"

from datetime import datetime

def convert(time):
    return time.strftime("%H:%M:%S,") + f"{time.microsecond // 1000:03d}"