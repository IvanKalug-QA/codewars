# The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.
#
# Good luck!
#
# If you like substring Katas, please try:

def solve(s):
    for i in range(len(s)):
        if s[i] not in 'aeiou':
            s = s.replace(s[i], '_')
    l = s.split('_')
    m = 0
    for i in l:
        if m < len(i):
            m = len(i)
    return m