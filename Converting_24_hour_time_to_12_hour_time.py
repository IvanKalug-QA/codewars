# Converting a 24-hour time like "0830" or "2030" to a 12-hour time (like "8:30 am" or "8:30 pm") sounds easy enough, right? Well, let's see if you can do it!

# You will have to define a function named "to12hourtime", and you will be given a four digit time string (in "hhmm" format) as input.

# Your task is to return a 12-hour time string in the form of "h:mm am" or "h:mm pm". (Of course, the "h" part will be two digits if the hour is greater than 9.)

def to_12_hour_time(time_string):
    hours = int(time_string[:2])
    minutes = time_string[2:]
    
    if hours == 0:
        return f"12:{minutes} am"
    elif hours < 12:
        return f"{hours}:{minutes} am"
    elif hours == 12:
        return f"12:{minutes} pm"
    else:
        return f"{hours - 12}:{minutes} pm"