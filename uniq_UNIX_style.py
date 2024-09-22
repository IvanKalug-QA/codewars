# Implement a function which behaves like the uniq command in UNIX.
#
# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.
#
# Example:
#
# ["a", "a", "b", "b", "c", "a", "b", "c"]  =>  ["a", "b", "c", "a", "b", "c"]

def uniq(seq):
    result = list()
    l = 0
    r = 0
    while r < len(seq):
        if seq[l] == seq[r]:
            r += 1
        else:
            result.append(seq[l])
            l = r
    if seq:
        result.append(seq[l])
    return result