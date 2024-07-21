# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
#
# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"

def what_century(year):
    cent = str((int(year) - 1) // 100 + 1)
    if int(cent) > 20:
        return cent + {'1': 'st', '2': 'nd', '3': 'rd'}.get(cent[1], 'th')
    else:
        return cent + 'th'