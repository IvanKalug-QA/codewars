# Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
# For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']

def spacey(array):
    l = [array[0]]
    for i in range(1, len(array)):
        l.append(l[-1] + array[i])
    return l