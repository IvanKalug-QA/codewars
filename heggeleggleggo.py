# Egg Talk.

# Insert an egg after each consonant. If there are no consonants, there will be no eggs. Argument will consist of a string with only alphabetic characters and possibly some spaces.

# Example
# hello => heggeleggleggo

# eggs => egegggeggsegg

# FUN KATA => FeggUNegg KeggATeggA

def heggeleggleggo(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        if char.isalpha() and char not in vowels:
            result += char + "egg"
        else:
            result += char
    return result