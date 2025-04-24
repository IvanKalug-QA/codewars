# Introduction
# The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.
#
# The most frequently used key is "GA-DE-RY-PO-LU-KI".
#
#  G => A
#  g => a
#  a => g
#  A => G
#  D => E
#   etc.
# The letters, which are not on the list of substitutes, stays in the encrypted text without changes.
#
# Task
# Your task is to help scouts to encrypt and decrypt thier messages. Write the Encode and Decode functions.
#
# Input/Output
# The input string consists of lowercase and uperrcase characters and white . The substitution has to be case-sensitive.
#
# Example
#  Encode("ABCD")          // => GBCE
#  Encode("Ala has a cat") // => Gug hgs g cgt
#  Encode("gaderypoluki"); // => agedyropulik
#  Decode("Gug hgs g cgt") // => Ala has a cat
#  Decode("agedyropulik")  // => gaderypoluki
#  Decode("GBCE")          // => ABCD

cipher = {
    'G': 'A', 'g': 'a', 'A': 'G', 'a': 'g', 'D': 'E', 'E': 'D',
    'd': 'e', 'e': 'd', 'E': 'D', 'E': 'D', 'e': 'd', 'e': 'd',
    'R': 'Y', 'Y': 'R', 'r': 'y', 'y': 'r', 'P': 'O', 'O': 'P',
    'p': 'o', 'o': 'p', 'L': 'U', 'U': 'L', 'l': 'u', 'u': 'l',
    'K': 'I', 'I': 'K', 'k': 'i', 'i': 'k'}


def encode(message):
    result = []
    for i in message:
        if i in cipher:
            result.append(cipher[i])
        else:
            result.append(i)
    return ''.join(result)


def decode(message):
    result = []
    for i in message:
        if i in cipher:
            result.append(cipher[i])
        else:
            result.append(i)
    return ''.join(result)cipher = {
    'G': 'A', 'g': 'a', 'A': 'G', 'a': 'g', 'D': 'E', 'E': 'D',
    'd': 'e', 'e': 'd', 'E': 'D', 'E': 'D', 'e': 'd', 'e': 'd',
    'R': 'Y', 'Y': 'R', 'r': 'y', 'y': 'r', 'P': 'O', 'O': 'P',
    'p': 'o', 'o': 'p', 'L': 'U', 'U': 'L', 'l': 'u', 'u': 'l',
    'K': 'I', 'I': 'K', 'k': 'i', 'i': 'k'}

def encode(message):
    result = []
    for i in message:
        if i in cipher:
            result.append(cipher[i])
        else:
            result.append(i)
    return ''.join(result)

def decode(message):
    result = []
    for i in message:
        if i in cipher:
            result.append(cipher[i])
        else:
            result.append(i)
    return ''.join(result)