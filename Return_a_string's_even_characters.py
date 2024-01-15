# Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".
#
# For example:
#
# "abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
# "a"             --> "invalid string"

def even_chars(st):
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    l = []
    count = 1
    for i in range(len(st)):
        if count % 2 == 0:
            l += [st[i]]
            count += 1
        else:
            count += 1
    return l