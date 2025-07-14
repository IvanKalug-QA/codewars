# This kata requires you to convert minutes (int) to hours and minutes in the format hh:mm (string).
#
# If the input is 0 or negative value, then you should return "00:00"
#
# Hint: use the modulo operation to solve this challenge. The modulo operation simply returns the remainder after a division. For example the remainder of 5 / 2 is 1, so 5 modulo 2 is 1.
#
# Example
# If the input is 78, then you should return "01:18", because 78 minutes converts to 1 hour and 18 minutes.
#
# Good luck! :D

def time_convert(num):
    if num < 0:
        return "00:00"
    hour = num // 60
    min = num % 60
    h = str(hour)
    m = str(min)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    return f"{h}:{m}"