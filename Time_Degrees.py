# Time, time, time. Your task is to write a function that will return the degrees on a analog clock from a digital time that is passed in as parameter. The digital time is of type string and will be in the format 00:00.

# Discrete hour hand movement is required - snapping to each hour position and also coterminal angles are not allowed.

# You also need to return the degrees on the analog clock in type string and format 360:360 . Remember to round off the degrees. Remember the basic time rules and format like 24:00 = 00:00 and 12:60 = 13:00.

# Create your own validation that should return "Check your time !" in any case the time is incorrect or the format is wrong , remember this includes passing in negatives times like "-01:-10".

# Examples
# "00:00" --> "360:360"
# "01:01" --> "30:6"
# "00:01" --> "360:6"
# "01:00" --> "30:360"
# "01:30" --> "30:180"
# "24:00" --> "Check your time !"
# "13:60" --> "Check your time !"
# "20:34" --> "240:204"
# Goodluck and Enjoy !


def clock_degree(s) :
    try:
        if len(s) != 5 or s[2] != ':':
            return "Check your time !"
        hours_str, minutes_str = s.split(':')
        if not (hours_str.isdigit() and minutes_str.isdigit()):
            return "Check your time !"
        hours = int(hours_str)
        minutes = int(minutes_str)
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            return "Check your time !"
        hour_deg = (hours % 12) * 30
        if hour_deg == 0:
            hour_deg = 360
        minute_deg = minutes * 6
        if minute_deg == 0:
            minute_deg = 360
        return f"{hour_deg}:{minute_deg}"
    except:
        return "Check your time !"