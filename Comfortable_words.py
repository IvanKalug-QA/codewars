# A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).
#
# That being said, complete the function which receives a word and returns true if it's a comfortable word and false otherwise.
#
# The word will always be a string consisting of only ascii letters from a to z.
#
#
#
# To avoid problems with image availability, here's the lists of letters for each hand:
#
# Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
# Right: y, u, i, o, p, h, j, k, l, n, m
# Examples
# "yams"  -->  true
# "test"  -->  false

def comfortable_word(word):
    left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    l = list()
    for i in word:
        if i in left:
            l.append('left')
        elif i in right:
            l.append('right')
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            return False
    return True