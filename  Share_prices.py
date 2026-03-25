# Share price
# You spent all your saved money to buy some shares.

# You bought it for invested, and want to know how much it's worth, but all the info you can quickly get are just the change the shares price made in percentages.

# Your task:
# Write the function sharePrice() that calculates, and returns the current price of your share, given the following two arguments:

# invested(number), the amount of money you initially invested in the given share

# changes(array of numbers), contains your shares daily movement percentages

# The returned number, should be in string format, and it's precision should be fixed at 2 decimal numbers.

# Have fun!

# Hint: Try to write the function in a functional manner!

from functools import reduce

def share_price(invested, changes):
    result = reduce(lambda price, change: price * (1 + change / 100), changes, invested)
    return f"{result:.2f}"