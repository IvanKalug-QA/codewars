# Computing the entropy of a message
# Information Theory
# In information theory, entropy is a measure of the uncertainty or randomness in a message. Entropy measures the average information per symbol: higher entropy means more unpredictability. Claude Shannon defined it in 1948. The Shannon entropy is calculated as:

# H
# =
# −
# ∑
# p
# i
# ⋅
# l
# o
# g
# 2
# (
# p
# i
# )
# H=−∑p 
# i
# ​
#  ⋅log 
# 2
# ​
#  (p 
# i
# ​
#  )

# where 
# p
# i
# p 
# i
# ​
#   is the probability of symbol 
# i
# i in the message. To calculate 
# p
# i
# p 
# i
# ​
#   count how many times each symbol appears in the message and divide by the total number of symbols. Each unique symbol should only be considered once in the sum. Note: spaces are not considered as informative symbols.

# For example in the message "foo" :

# f appears 1 time out of 3 symbols: 
# p
# f
# =
# 1
# /
# 3
# p 
# f
# ​
#  =1/3
# o appears 2 times out of 3 symbols: 
# p
# o
# =
# 2
# /
# 3
# p 
# o
# ​
#  =2/3
# Thus, the entropy is: 
# −
# (
# 1
# /
# 3
# ⋅
# l
# o
# g
# 2
# (
# 1
# /
# 3
# )
# +
# 2
# /
# 3
# ⋅
# l
# o
# g
# 2
# (
# 2
# /
# 3
# )
# )
# ≈
# 0.918295834
# −(1/3⋅log 
# 2
# ​
#  (1/3)+2/3⋅log 
# 2
# ​
#  (2/3))≈0.918295834

# Watch a video about Shannon entropy for more context.

# Use Case
# You are analyzing a collection of messages from different sources and want to determine which ones are more compressible. By calculating the entropy of each message, you can estimate their unpredictability: messages with lower entropy contain more repeated or predictable patterns and are therefore easier to compress, while messages with higher entropy are more random and less compressible. This allows you to prioritize storage or transmission strategies based on how efficiently each message can be handled.

# Task
# Write a function that receives a message (string) and returns the Shannon entropy (float) of the message.

# Notes
# Use the math library for logarithm calculations
# If the message is empty, return 0.0

import math

def entropy(message: str) -> float:
    if not message:
        return 0.0
    
    message = message.replace(" ", "")
    if not message:
        return 0.0
    
    char_count = {}
    for char in message:
        char_count[char] = char_count.get(char, 0) + 1
    
    total_symbols = len(message)
    
    entropy_value = 0.0
    for count in char_count.values():
        probability = count / total_symbols
        entropy_value -= probability * math.log2(probability)
    
    return entropy_value