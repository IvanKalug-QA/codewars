# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
#
# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
#
# The left side letters and their power:
#
#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:
#
#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims.
#
# Example
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!

def alphabet_war(fight):
    le = {
        'w': 4, 'p': 3,
        'b': 2, 's': 1
    }
    ri = {
        'm': 4, 'q': 3,
        'd': 2, 'z': 1
    }
    rig = 0
    lef = 0
    for i in fight:
        if i in ri:
            rig += ri[i]
        elif i in le:
            lef += le[i]
    if rig > lef:
        return "Right side wins!"
    elif lef > rig:
        return "Left side wins!"
    else:
        return "Let's fight again!"