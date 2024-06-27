# Implement the method indexOf (index_of in PHP), which accepts a linked list (head) and a value, and returns the index (zero based) of the first occurrence of that value if exists, or -1 otherwise.
#
# For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, indexOf / index_of should return 2.
#
# The linked list is defined as follows:
#
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# Note: the list may be null and can hold any type of value.
#
# Good luck!

def index_of(head, value):
    if head is None:
        return -1
    current = head
    count = 0
    while current.next:
        if current.data == value:
            return count
        else:
            count += 1
            current = current.next
    return -1