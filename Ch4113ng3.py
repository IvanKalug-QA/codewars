# Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"

def nerdify(txt):
    d = {
        'a': '4',
        'A': '4',
        'e': '3',
        'E': '3',
        'l': '1',
    }
    for i in txt:
        for k,v in d.items():
            if i == k:
                txt = txt.replace(i,v)
    return txt