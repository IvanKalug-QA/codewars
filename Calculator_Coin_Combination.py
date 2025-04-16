# The function takes cents value (int) and needs to return the minimum number of coins combination of the same value.
#
# The function should return an array where
# coins[0] = pennies ==> $00.01
# coins[1] = nickels ==> $00.05
# coins[2] = dimes ==> $00.10
# coins[3] = quarters ==> $00.25
#
# So for example:
# coinCombo(6) --> [1, 1, 0, 0]


def coin_combo(cents):
    coins = [25, 10, 5, 1]
    result = [0, 0, 0, 0]
    for i in range(len(coins)):
        if not cents:
            return result[::-1]
        if cents - coins[i] >= 0:
            result[i] += cents // coins[i]
            cents -= coins[i]  * (cents // coins[i])
    return result[::-1]