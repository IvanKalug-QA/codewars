# A very easy task for you!

# You have to create a method, that corrects a given date string. There was a problem in addition, so many of the date strings are broken. Date-Format is european. That means "DD.MM.YYYY".

# Some examples:

# "30.02.2016" -> "01.03.2016"
# "40.06.2015" -> "10.07.2015"
# "11.13.2014" -> "11.01.2015"
# "99.11.2010" -> "07.02.2011"

# If the input-string is null or empty return exactly this value!
# If the date-string-format is invalid, return null.

# Hint: Correct first the month and then the day!

# Have fun coding it and please don't forget to vote and rank this kata! :-)

# I have created other katas. Have a look if you like coding and challenges.

def date_correct(date):
    if not date:
        return date
    
    parts = date.split('.')
    if len(parts) != 3:
        return None
    
    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return None
    
    try:
        day, month, year = map(int, parts)
    except:
        return None
    
    extra_years = (month - 1) // 12
    year += extra_years
    month = (month - 1) % 12 + 1
    
    def days_in_month(m, y):
        if m == 2:
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                return 29
            return 28
        if m in [4, 6, 9, 11]:
            return 30
        return 31
    
    while True:
        dim = days_in_month(month, year)
        if day <= dim:
            break
        day -= dim
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    return f"{day:02d}.{month:02d}.{year}"