# The notorious Captain Schneider has given you a very straightforward mission. Any data that comes through the system make sure that only non-special characters see the light of day.
#
# Create a function that given a string, retains only the letters A-Z (upper and lowercase), 0-9 digits, and whitespace characters. Also, returns "Not a string!" if the entry type is not a string.

def nothing_special(st):
    if not isinstance(st, str):
        return "Not a string!"
    result = []
    for i in st:
        if i.isalpha() or i in " \t\r\n\x0b\x0c" or i in "0123456789":
            result.append(i)
    return "".join(result)