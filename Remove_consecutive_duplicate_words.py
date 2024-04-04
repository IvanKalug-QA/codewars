# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:
#
# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
#
# --> "alpha beta gamma delta alpha beta gamma delta"
# Words will be separated by a single space. There will be no leading or trailing spaces in the string. An empty string (0 words) is a valid input.

def remove_consecutive_duplicates(s : str) -> str:
    if not s:
        return ''
    l = list()
    prev = ''
    for i in s.split():
        if i != prev:
            l.append(i)
            prev = i
    return ' '.join(l)