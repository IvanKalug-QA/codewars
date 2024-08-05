# Write a function that determines whether the passed in sequences are similar. Similar means they contain the same elements, and the same number of occurrences of elements.
#
# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 1, 2, 4, 3]
# arr3 = [1, 2, 3, 4]
# arr4 = [1, 2, 3, "4"]
# arrays_similar(arr1, arr2) # Should equal true
# arrays_similar(arr2, arr3) # Should equal false
# arrays_similar(arr3, arr4) # Should equal false

def arrays_similar(seq1, seq2):
    if len(seq1) != len(seq2):
        return False
    for i in seq1:
        if seq1.count(i) != seq2.count(i):
            return False
    return True