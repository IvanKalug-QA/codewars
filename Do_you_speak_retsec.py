# DESCRIPTION:
# Do you speak retsec?
# You and your friends want to play undercover agents. In order to exchange your secret messages, you've come up with the following system: you take the word, cut it in half, and place the first half behind the latter. If the word has an uneven number of characters, you leave the middle at its previous place:
#
# retsec examples
#
# That way, you'll be able to exchange your messages in private.
#
# Task
# You're given a single word. Your task is to swap the halves. If the word has an uneven length, leave the character in the middle at that position and swap the chunks around it.
#
# Examples
# reverse_by_center("secret")  == "retsec" # no center character
# reverse_by_center("agent")   == "nteag"  # center character is "e"
# Remarks
# Don't use this to actually exchange messages in private.

def reverse_by_center(s):
    r = ''
    t = 0
    if len(s) % 2 == 0:
        f = len(s) // 2
        r = s[f::] + s[:f]
        return r
    f = len(s)
    for i in range(f + 1):
        t += i
    t = t // f
    g = t - 1
    return s[t::] + s[g] + s[:t - 1]