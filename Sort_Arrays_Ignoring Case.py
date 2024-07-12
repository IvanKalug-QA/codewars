# Sort the given array of strings in alphabetical order, case insensitive. For example:
#
# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

def sortme(words):
    l = [i.lower() for i in words]
    l.sort()
    res = []
    for i in l:
        for j in words:
            if i == j.lower():
                res.append(j)
    return res