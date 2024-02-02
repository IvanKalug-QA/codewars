# Failed Filter - Bug Fixing #3
# Oh no, Timmy's filter doesn't seem to be working? Your task is to fix the FilterNumber function to remove all the numbers from the string.

def filter_numbers(s):
    for i in s:
        if i.isdigit():
            s = s.replace(i,'')
    return s