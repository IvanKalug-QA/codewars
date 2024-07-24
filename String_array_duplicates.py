# In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.
#
# For example:
#
# dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
#
# dup(["kelless","keenness"]) = ["keles","kenes"].
#
# Strings will be lowercase only, no spaces. See test cases for more examples.
#
# Good luck!

def dup(arry):
    l = list()
    for i in arry:
        ar = list()
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                if len(ar):
                    if ar[-1] != i[j]:
                        ar.append(i[j])
                else:
                    ar.append(i[j])
            else:
                if len(ar):
                    if ar[-1] != i[j]:
                        ar.append(i[j])
                else:
                    ar.append(i[j])
        if i[-1] != ar[-1]:
            ar.append(i[-1])
        l.append(''.join(ar))
        ar = []
    return l