# Goal
# Given a list of elements [a1, a2, ..., an], with each ai being a string, write a function majority that returns the value that appears the most in the list.
#
# If there's no winner, the function should return None, NULL, nil, etc, based on the programming language.
#
# Example
# majority(["A", "B", "A"]) returns "A"
# majority(["A", "B", "B", "A"]) returns None

from collections import Counter


def majority(arr):
    if not arr:
        return None

    c = Counter(arr)
    max_count = max(c.values())

    winners = [item for item, count in c.items() if count == max_count]

    if len(winners) == 1:
        return winners[0]
    else:
        return None