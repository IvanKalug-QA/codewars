# You are the rock paper scissors oracle.
#
# Famed throughout the land, you have the incredible ability to predict which hand gestures your opponent will choose out of rock, paper and scissors.
#
# Unfortunately you're no longer a youngster, and have trouble moving your hands between rounds. For this reason, you can only pick a single gesture for each opponent. If it's possible for you to win, you will, but you're also happy to tie.
#
# Given an array of gestures — for example ["paper", "scissors", "scissors"] — return the winning gesture/s in the order in which they appear in the title, separated by a forward slash. For example, if rock and scissors could both be used to win you would return:
#
# "rock/scissors"
#
# If it's not possible for you to win then return:
#
# "tie"
#
# See https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors if you're not familiar with rock paper scissors.
#
# Second attempt at my first Kata...

def oracle(gestures):
    possible_gestures = ["rock", "paper", "scissors"]
    winning_gestures = []

    for my_gesture in possible_gestures:
        wins = 0
        losses = 0

        for opponent_gesture in gestures:
            if my_gesture == opponent_gesture:
                continue
            elif (my_gesture == "rock" and opponent_gesture == "scissors") or \
                    (my_gesture == "scissors" and opponent_gesture == "paper") or \
                    (my_gesture == "paper" and opponent_gesture == "rock"):
                wins += 1
            else:
                losses += 1

        if wins > losses:
            winning_gestures.append(my_gesture)

    if not winning_gestures:
        return "tie"
    else:
        return "/".join(winning_gestures)