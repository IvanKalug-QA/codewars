# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.
#
# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
#
# Test examples:
#
# "EBG13 rknzcyr." -> "ROT13 example."
#
# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

from string import ascii_lowercase, ascii_uppercase
def rot13(message):
    result = []
    upper = ascii_uppercase
    lower = ascii_lowercase
    for i in message:
        if i in upper:
            idx = (upper.index(i) + 13) % 26
            result.append(upper[idx])
        elif i in lower:
            idx = (lower.index(i) + 13) % 26
            result.append(lower[idx])
        else:
            result.append(i)
    return ''.join(result)