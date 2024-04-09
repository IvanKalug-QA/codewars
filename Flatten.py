# Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.
#
# flatten [1,2,3] # => [1,2,3]
# flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
# flatten [[[1,2,3]]] # => [[1,2,3]]

def flatten(lst):
    l = []
    for i in lst:
        if type(i) == int or type(i) == str or type(i) == float:
            l.append(i)
        else:
            l += i
    return l