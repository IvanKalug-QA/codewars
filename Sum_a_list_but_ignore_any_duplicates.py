# Please write a function that sums a list, but ignores any duplicate items in the list.
#
# For instance, for the list [3, 4, 3, 6] , the function should return 10.

def sum_no_duplicates(l):
    d = {}
    for i in l:
        d[i] = d.get(i,0) + 1
    return sum([k for k,v in d.items() if v == 1])