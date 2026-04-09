# Raffle Run: What Are the Odds?
# You've entered multiple independent raffles back to back. Each raffle is a single-winner draw: one ticket is pulled from the pool, and if it's yours, you win.

# Given two arrays of equal length:

# totals — the total number of tickets sold in each raffle
# purchased — how many tickets you bought in each raffle
# Return your probability of winning at least one raffle as a simplified fraction string in the form "numerator/denominator". This fraction must be full reduced, so "4/8" becomes "1/2" and "9/12" becomes "3/4."

# Probability Hint
# For independent events, the probability of winning at least one is the complement of losing all of them:

# P(A or B or ...) = 1 - P(!A) * P(!B) * ...

# where P(!X) is the probability of not winning raffle X.

# Examples
# // One raffle, 1 ticket out of 3
# raffleOdds([3], [1])           // => "1/3"

# // Two raffles, 1 ticket each out of 4
# raffleOdds([4, 4], [1, 1])    // => "7/16"

# // Three raffles
# raffleOdds([2, 3, 6], [1, 1, 1])  // => "13/18"
# Notes
# All values are positive integers
# purchased[i] <= totals[i]
# If you've purchased no tickets in any given raffle, that raffle has no impact on your odds
# If you are guaranteed to win any single raffle, return "1/1"
# The returned fraction must be fully reduced


from math import gcd
from functools import reduce

def raffle_odds(totals, purchased):
    num = 1
    den = 1
    for total, bought in zip(totals, purchased):
        lose_num = total - bought
        lose_den = total
        num *= lose_num
        den *= lose_den
    win_num = den - num
    win_den = den
    g = gcd(win_num, win_den)
    win_num //= g
    win_den //= g
    return f"{win_num}/{win_den}"