# Given a number and a binary tree ( not a Binary Search Tree! ):

# return True/true if the given number is in the tree
# return False/false if it isn't

from preloaded import Node

def search(n: int, root: Node | None) -> bool:
    """Determines if a given number exists in the binary tree."""
    if root is None:
        return False
    
    if root.value == n:
        return True
    
    return search(n, root.left) or search(n, root.right)