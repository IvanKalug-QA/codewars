# DESCRIPTION:
# Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

def include(arr,item):
    for i in arr:
        if i == item:
            return True
    return False