# Introduction
# You are blindfolded, with n coins on a table. You know that k coins are heads up and the others are tails up, but not which ones are which.

# Task
# Divide the coins in two groups with the same number of heads in each group. You can flip the coins any number of times.

# Yuor method should work every time.

# Input
# ⬬ coins [list of Coin]
# The coins. Coins have a flip method that flips the coin and returns it.

# Examples:

# # flip the first coin
# coins[0].flip()

# # flip every third coin
# for coin in coins[2::3]:
#     coin.flip()
    
# # flip even coins and put them in a list
# [coin.flip() for coin in coins[::2]]
# ⬬ k [integer]
# The number of coins that are heads up.

# Output
# Two lists of coins, representing the two groups.

# The two lists together should contais all the coins exactly once (no missing coins, no duplicates).

# The number of coins heads up in first and second list should be the same.

def split_coins(coins, k):
    group1 = coins[:k]
    group2 = coins[k:]
    
    for coin in group1:
        coin.flip()
    
    return group1, group2