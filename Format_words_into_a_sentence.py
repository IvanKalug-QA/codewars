# Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string.
#
# Note:
#
# Empty string values should be ignored.
# Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
# Example: (Input --> output)
#
# ['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
# ['ninja', '', 'ronin'] --> "ninja and ronin"
# [] -->""

def format_words(words):
    if words is None or not words:
        return ''
    if len(words) == 1:
        return words[0]
    l = [i for i in words if i !=  '']
    if len(l) == 2:
        return ' and '.join(l)
    elif len(l) > 2:
        lost = l.pop()
        return ', '.join(l) + ' and ' + lost
    else:
        return l[0]