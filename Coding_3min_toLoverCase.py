# Task
# Yes, your eyes are no problem, this is toLoverCase (), not toLowerCase (), we want to make the world full of love.
#
# What do we need to do?
# You need to add a prototype function to the String, the name is toLoverCase. Function can convert the letters in the string, converted to "L", "O", "V", "E", if not the letter, don't change it.
#
# How to convert? :
# "love!".toLoverCase()="EVOL!"
#     "l" is 11th(start with 0) in lower case letters
#     abcdefghijklmnopqrstuvwxyz
#                |
#     0...      11----------------->11th letter
#     We use this number mod 4------> 11 % 4 = 3
#
#     the 3rd(also start with 0) letter of "LOVE" is "E"
#     LOVE
#        |
#        3--------->3rd letter
#
#     so convert "l" to "E".
#
#     and so on..
#
#     "o" convert to "V", "v" convert to "O", "e" convert to "L"
#
#     last "!" remain unchanged, because it's not a letter.

def to_lover_case(s):
    LOVE = "LOVE"
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for char in s:
        if char.isalpha():
            position = alphabet.index(char.lower())
            love_index = position % 4
            result += LOVE[love_index]
        else:
            result += char

    return result