# Algorithmic predicament - Bug Fixing #9
# Oh no! Timmy's algorithm has gone wrong! Help Timmy fix his algorithm!
#
# Task
# Your task is to fix Timmy's algorithm so it returns the group name with the highest total age.
#
# You will receive two groups of `people` objects, with two properties `name` and `age`. The name property is a string, and the age property is a number.
#
# Your goal is to calculate the total age of all people with the same name in both groups and return the name of the person with the highest total age. If two names have the same total age, return the first alphabetical name.

def highest_age(group1,group2):
    total = {}
    for person in group1 + group2:
        name = person['name']
        total[name] = total.get(name, 0) + person['age']
    max_name = None
    max_age = -1
    for name, age in total.items():
        if age > max_age or (age == max_age and name < max_name):
            max_name = name
            max_age = age
    return max_name