# You were given a string of integer temperature values, each separated by a space character.
#
# Create a function that return its lowest value, or None/null/Nothing if the string is empty.

def lowest_temp(t):
    return min(int(i) for i in t.split()) if t else None