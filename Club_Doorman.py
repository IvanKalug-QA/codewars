# INTRODUCTION
# The Club Doorman will give you a word. To gain access, you need to provide the right number according to the given word.
#
# Each word contains exactly one pair of consecutive identical letters, such as the tt in lettuce.
#
# To determine the number, find the position of the repeated letter in the alphabet (where a is 1, b is 2, ..., z is 26) and multiply it by 3.
#
# TASK
# Implement a function that takes a word as input and returns the correct number.
#
# EXAMPLE
# For the word lettuce, the repeated letter is t, which is the 20th letter in the alphabet.
#
# The correct answer is 20 × 3 = 60.
#
# NOTE
# You may assume that the given string will
#
# always contain exactly one pair of consecutive identical letters.
#
# consist only of lowercase English letters.

def pass_the_door_man(word):
    counter = {}
    left = 0
    for right in range(len(word)):
        if word[left] != word[right]:
            counter[word[left]] = max(counter.get(word[left], 0), right - left)
            left = right
    counter[word[left]] = max(counter.get(word[left], 0), len(word) - left)
    sym = ''
    score = 0
    for i in counter:
        if counter[i] > score:
            sym = i
            score = counter[i]
    return (ord(sym) - 96) * 3