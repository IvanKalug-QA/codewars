# Paul is an excellent coder and sits high on the CW leaderboard. He solves kata like a banshee but would also like to lead a normal life, with other activities. But he just can't stop solving all the kata!!
#
# Given an array (x) you need to calculate the Paul Misery Score. The values are worth the following points:
#
# kata = 5
# Petes kata = 10
# life = 0
# eating = 1
# The Misery Score is the total points gained from the array. Once you have the total, return as follows:
#
# < 40 = 'Super happy!'
# < 70 >= 40 = 'Happy!'
# < 100 >= 70 = 'Sad!'
# > 100 = 'Miserable!'

def paul(x):
    d = {'life': 0, 'eating': 1, 'Petes kata': 10, 'kata': 5}
    c = 0
    for i in x:
        c += d.get(i)
    if c < 40:
        return 'Super happy!'
    elif c >= 40 and c < 70:
        return 'Happy!'
    elif c < 100 and c >= 70:
        return 'Sad!'
    else:
        return 'Miserable!'