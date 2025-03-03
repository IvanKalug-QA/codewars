# Implement the method lastIndexOf (last_index_of in PHP and Python), which accepts a linked list (head) and a value, and returns the index (zero based) of the last occurrence of that value if exists, or -1 otherwise.
#
# For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, lastIndexOf / last_index_of should return 3.
#
# The linked list is defined as follows:
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# Note: the list may be null/None and can hold any type of value.
#
# Good luck!

def last_index_of(head, search_val):
    current = head
    result = -1
    idx = 0
    while current:
        if current.data == search_val:
            result = idx
        idx += 1
        current = current.next
    return result