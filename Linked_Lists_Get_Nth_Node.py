# Linked Lists - Get Nth
# Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on.
#
# So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13);
#
# getNth(1 -> 2 -> 3 -> null, 0).data === 1
# getNth(1 -> 2 -> 3 -> null, 1).data === 2
# The index should be in the range [0..length-1]. If it is not, or if the list is empty, GetNth() should throw/raise an exception (ArgumentException in C#, InvalidArgumentException in PHP, Exception in Java).

from preloaded import Node


# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None:
        raise "None linked list should throw error."
    if index == 0:
        return node
    current = node
    count = 0
    while current.next:
        if count == index:
            return current
        count += 1
        current = current.next
    if index > count or index < 0:
        raise 'Invalid index value should throw error.'
    return current
    # Your code goes here.