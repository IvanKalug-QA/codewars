# Gordon Ramsay shouts. He shouts and swears. There may be something wrong with him.
#
# Anyway, you will be given a string of four words. Your job is to turn them in to Gordon language.
#
# Rules:
#
# Obviously the words should be Caps, Every word should end with '!!!!', Any letter 'a' or 'A' should become '@', Any other vowel should become '*'.

def gordon(a):
    l = a.split()
    ls = list()
    ll = list()
    for i in l:
        i = i.upper()
        if "A" in i:
            i = i.replace('A', '@')
            ls.append(i + '!!!!')
        else:
            ls.append(i + '!!!!')
    for i in ls:
        for j in ['O', 'E', 'I', "U"]:
            if j in i:
                i = i.replace(j,'*')
        ll.append(i)
    return ' '.join(ll)