# Implement the method length, which accepts a linked list (head), and returns the length of the list.
#
# For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.
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

def length(head):
    if head is None:
        return 0
    count = 0
    current = head
    while current.next:
        count += 1
        current = current.next
    return count + 1