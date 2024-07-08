# Acknowledgments:
# I thank yvonne-liu for the idea and for the example tests :)
#
# Description:
# Encrypt this!
#
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
#
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    if not len(text):
        return ''
    l = list()
    ll = list()
    for i in text.split():
        f = i[1] if len(i) > 1 else ''
        f2 = i[-1] if len(i) > 1 else ''
        for j in range(len(i)):
            if j == 0:
                ll.append(str(ord(i[j])))
            elif j == 1:
                ll.append(f2)
            elif j == len(i) - 1:
                ll.append(f)
            else:
                ll.append(i[j])
        l.append(''.join(ll))
        ll = []
    return ' '.join(l)