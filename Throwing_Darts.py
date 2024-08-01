# You've just recently been hired to calculate scores for a Dart Board game!
#
# Scoring specifications:
#
# 0 points - radius above 10
# 5 points - radius between 5 and 10 inclusive
# 10 points - radius less than 5
# If all radii are less than 5, award 100 BONUS POINTS!
#
# Write a function that accepts an array of radii (can be integers and/or floats), and returns a total score using the above specification.
#
# An empty array should return 0.
#
# Examples:
# scoreThrows( [1, 5, 11] )    =>  15
# scoreThrows( [15, 20, 30] )  =>  0
# scoreThrows( [1, 2, 3, 4] )  =>  140

def score_throws(radii):
    if not len(radii):
        return 0
    count = 0
    re = 0
    for i in radii:
        if i > 10:
            count += 0
        elif i >= 5 and i <= 10:
            count += 5
        elif i < 5:
            count += 10
            re += 1
    if re == len(radii):
        count += 100
    return count