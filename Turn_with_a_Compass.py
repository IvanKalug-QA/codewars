# You have an 8-wind compass, like this:

# You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW) and a certain degree to turn (a multiple of 45, between -1080 and 1080); positive means clockwise, and negative means counter-clockwise.

# Return the direction you will face after the turn.

# Examples
# "S",  180  -->  "N"
# "SE", -45  -->  "E"
# "W",  495  -->  "NE"

def direction(facing, turn):
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    start_index = compass.index(facing)
    steps = turn // 45
    new_index = (start_index + steps) % 8
    return compass[new_index]