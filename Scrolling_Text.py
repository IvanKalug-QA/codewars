# Let's create some scrolling text!
#
# Your task is to complete the function which takes a string, and returns an array with all possible rotations of the given string, in uppercase.
#
# Example
# scrollingText("codewars") should return:
#
# [ "CODEWARS",
#   "ODEWARSC",
#   "DEWARSCO",
#   "EWARSCOD",
#   "WARSCODE",
#   "ARSCODEW"
#   "RSCODEWA",
#   "SCODEWAR" ]
# Good luck!

def scrolling_text(text):
    result = [text.upper()]
    text = text.upper()
    n = len(text)
    for i in range(n):
        text += text[0]
        text = text[1::]
        result.append(text)
    return result[:-1]