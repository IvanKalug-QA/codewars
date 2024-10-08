# You will be given a sequence of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return:
#
# true if all of the following continents / geographic zones will be represented by at least one developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
# false otherwise.
# For example, given the following input array:
#
# list1 =  [
#   { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
#   { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
#   { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
#   { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
#   ]
# your function should return true as there is at least one developer from the required 5 geographic zones.
#
# Notes:
#
# The input array and continent names will always be valid and formatted as in the list above for example 'Africa' will always start with upper-case 'A'.
#
#
#
#
# This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: forEach, filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible.

def all_continents(lst):
    d = dict()
    for i in lst:
        d[i['continent']] = d.get(i['continent'], 0) + 1
    res = list()
    for i in d:
        if i in ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']:
            if i not in res:
                res.append(i)
    return len(res) == len(['Africa', 'Americas', 'Asia', 'Europe', 'Oceania'])