# Write a program that will calculate the date that someone turned or will celebrate their next 1 Gs anniversary.

# You are a given a date as parameter and you need to return the date of 1 Gs from the given date.

# A gigasecond is one billion (10**9) seconds.

# Examples
#   2011-04-25  ->  2043-01-01
#   1977-06-13  ->  2009-02-19
# Assumptions
# You can assume that you are only given a valid date object.

from datetime import datetime, timedelta

def gigasecond(start_date):
    GIGASECOND = 10**9
    return start_date + timedelta(seconds=GIGASECOND)