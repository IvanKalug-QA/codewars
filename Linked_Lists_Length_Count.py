# Linked Lists - Length & Count
#
# Implement length to count the number of nodes in a linked list.
#
# length(null) => 0
# length(1 -> 2 -> 3 -> null) => 3
# Implement Count() to count the occurrences of an integer in a linked list.
#
# count(null, 1) => 0
# count(1 -> 2 -> 3 -> null, 1) => 1
# count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
# I've decided to bundle these two functions within the same Kata since they are both very similar.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    leng = 0
    current = node
    while current:
        leng += 1
        current = current.next
    return leng


def count(node, data):
    dig = 0
    current = node
    while current:
        if current.data == data:
            dig += 1
        current = current.next
    return dig