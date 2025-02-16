# Overview
# Many people know that Apple uses the letter "i" in almost all of its devices to emphasize its personality.
#
# And so John, a programmer at Apple, was given the task of making a program that would add that letter to every word. Let's help him do it, too.
#
# Task:
# Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the word. For example we get the word "Phone", so we must return "iPhone". But we have a few rules:
#
# The word should not begin with the letter "I", for example Inspire.
# The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace. ("y" is considered a consonant)
# The first letter should not be lowercase, for example road.
# If the word does not meet the rules, we return "Invalid word".

def i(word):
    s = ('a', 'e', 'i', 'o', 'u')
    d = {'v': 0, 'c': 0}
    for i in word:
        if i.lower() in s:
            d['v'] += 1
        else:
            d['c'] += 1
    return 'i' + word if word and word[0].isupper() and word[0] != 'I' and d['c'] > d['v'] else "Invalid word"