# Write a function that takes a string and returns an array containing binary numbers equivalent to the ASCII codes of the characters of the string. The binary strings should be eight digits long.
#
# Example: 'man' should return [ '01101101', '01100001', '01101110' ]

def word_to_bin(word):
    return ['0' + bin(ord(i))[2::] for i in word]