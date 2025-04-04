# Oh no! Ghosts have reportedly swarmed the city. It's your job to get rid of them and save the day!
#
# In this kata, strings represent buildings while whitespaces within those strings represent ghosts.
#
# So what are you waiting for? Return the building(string) without any ghosts(whitespaces)!
#
# Example:
#
# "Sky scra per" -> "Skyscraper"
# If the building contains no ghosts, return the string:
#
# "You just wanted my autograph didn't you?"

def ghostbusters(building):
    return ''.join(i.strip() for i in building) if ' ' in building else "You just wanted my autograph didn't you?"