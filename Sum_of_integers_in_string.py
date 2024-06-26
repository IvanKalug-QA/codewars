# Your task in this kata is to implement a function that calculates the sum of the integers inside a string. For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.
#
# Note: only positive integers will be tested.

def sum_of_integers_in_string(s):
    l = list()
    for i in s:
        if not i.isdigit():
            s = s.replace(i, '_')
    for i in s.split('_'):
        if i.isdigit():
            l.append(int(i))
    return sum(l) if l else 0