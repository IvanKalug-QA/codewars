# Task
# Given a string, return the number of lonely letters it contains.

# A letter is lonely when:

# It appears exactly once in the whole string.
# Its alphabetical neighbors are both absent from the string.
# Alphabetical neighbors are the previous and next letters in the alphabet.

# d has alphabetical neighbors c and e.
# a has only one possible neighbor: b.
# z has only one possible neighbor: y.
# The alphabet is not cyclic, so z is not a neighbor of a, and a is not a neighbor of z.
# For example:

# d is not lonely if c or e also appears somewhere in the text.
# m is lonely if m appears once and both l and n are absent.
# Rules
# Ignore letter case.
# Ignore all non-letter characters.
# Work only with English letters a-z.
# Examples
# Input: "ad" -> Output: 2
# Input: "abc" -> Output: 0
# Input: "Hello, World!" -> Output: 3
# Input: "A-dA" -> Output: 1
# Input: "zz" -> Output: 0

def count_lonely_letters(text):
    text = text.lower()
    counts = {}
    for ch in text:
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    
    lonely = 0
    for ch, cnt in counts.items():
        if cnt == 1:
            prev_ch = chr(ord(ch) - 1) if ch > 'a' else ''
            next_ch = chr(ord(ch) + 1) if ch < 'z' else ''
            if (not prev_ch or prev_ch not in counts) and (not next_ch or next_ch not in counts):
                lonely += 1
    return lonely