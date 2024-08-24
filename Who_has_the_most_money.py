# You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:
#
# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
# As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".
#
# Notes:
#
# Each student will have a unique name
# There will always be a clear winner: either one person has the most, or everyone has the same amount
# If there is only one student, then that student has the most money

def most_money(students):
    count = 0
    l = list()
    for i in students:
        count += i.fives * 5
        count += i.tens * 10
        count += i.twenties * 20
        l.append((count, i.name))
        count = 0
    l.sort()
    if len(l) == 1:
        return l[0][1]
    count = 0
    m = 0
    n = ''
    for i, v in l:
        if i > m:
            m = i
            n = v
        elif i == m:
            count += 1
    if count == len(l) - 1:
        return 'all'
    return n