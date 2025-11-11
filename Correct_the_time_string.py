# A new task for you!

# You have to create a method, that corrects a given time string.
# There was a problem in addition, so many of the time strings are broken.
# Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.
# Examples
# "09:10:01" -> "09:10:01"  
# "11:70:10" -> "12:10:10"  
# "19:99:99" -> "20:40:39"  
# "24:01:01" -> "00:01:01"  
# If the input-string is null or empty return exactly this value! (empty string for C++) If the time-string-format is invalid, return null. (empty string for C++)

# Have fun coding it and please don't forget to vote and rank this kata! :-)

# I have created other katas. Have a look if you like coding and challenges.

def time_correct(t):
    if t is None or t == "":
        return t
    if len(t) != 8 or t[2] != ':' or t[5] != ':':
        return None
    parts = t.split(':')
    for part in parts:
        if not part.isdigit():
            return None
    hours, minutes, seconds = map(int, parts)
    
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60
    
    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60
    
    if hours >= 24:
        hours = hours % 24
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"