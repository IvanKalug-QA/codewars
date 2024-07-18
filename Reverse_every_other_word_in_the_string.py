# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

def reverse_alternate(st):
    l = [i.strip() for i in st.split()]
    for i in range(1, len(l), 2):
        l[i] = l[i][::-1]
    return ' '.join(l)