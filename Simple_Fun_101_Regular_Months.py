# Task
# In an effort to be more innovative, your boss introduced a strange new tradition: the first day of every month you're allowed to work from home. You like this rule when the day falls on a Monday, because any excuse to skip rush hour traffic is great!

# You and your colleagues have started calling these months regular months. Since you're a fan of working from home, you decide to find out how far away the nearest regular month is, given that the currMonth has just started.

# For your convenience, here is a list of month lengths (from January to December, respectively):

#  Month lengths: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31. Please, note that in leap years February has 29 days.

# Example
# For currMonth = "02-2016", the output should be "08-2016".

# February of 2016 year is regular, but it doesn't count since it has started already, so the next regular month is August of 2016 - which is the answer.

# Input/Output
# [input] string currMonth

# A string representing the correct month in the format mm-yyyy, where mm is the number of the month (1-based, i.e. 01 for January, 02 for February and so on) and yyyy is the year.

# Constraints:

# 1 ≤ int(mm) ≤ 12,

# 1970 ≤ int(yyyy) ≤ 2100.

# [output] a string

# The earliest regular month after the given one in the same format as currMonth.


def regular_months(curr_month):
    m_str, y_str = curr_month.split('-')
    m = int(m_str)
    y = int(y_str)
    m += 1
    if m > 12:
        m = 1
        y += 1
    
    def is_monday_first(month, year):
        q = 1
        if month < 3:
            month += 12
            year -= 1
        K = year % 100
        J = year // 100
        h = (q + (13*(month+1))//5 + K + K//4 + J//4 - 2*J) % 7
        return h == 2
    
    while True:
        if is_monday_first(m, y):
            return f"{m:02d}-{y}"
        m += 1
        if m > 12:
            m = 1
            y += 1