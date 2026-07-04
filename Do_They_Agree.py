# Situation
# Alice and Bob work in an office. Sometimes they play word-games when the boss is out, but today (Tuesday) their boss sent an urgent memo to the entire office, and now they have some actual "work" to do.

# The memo instructed everyone to create their own individual (list) of ID numbers referencing employees with whom they spoke during the staff meeting held yesterday (Monday). But the memo made it urgently clear: numbers should not be based on when you spoke, but instead they must be ordered by when the employee actually showed up to the meeting.

# Lastly, the memo stated that there would be a tribunal hearing of evidence held the following day (Wednesday) to vet the data. (Be sure to also solve the following kata about tomorrow's hearing). So Alice and Bob dutifully got to work today, preparing their own (list)s. But afterwards they were left pondering one thing; did at least their own (list)s agree with each other in terms of office employee arrival times?


# Task
# Given two (list)s of numbers representing office employee ID's, determine whether or not all numbers in the 1st (list) correspond to the relationship of their order in the 2nd (list).


# Examples
# For these (list)s:

# [1, 2, 3, 5]
# [1, 3, 4]
# all of the numbers in the 1st (list) appear in an order that conforms to the numbers in the 2nd (list), so the function should return true.

# For these (list)s:

# [8, 5, 4, 3]
# [9, 8, 3, 1, 5]
# in the 1st (list) the number 3 appears after the number 5, whereas in the 2nd (list) it comes before, so the function should return false.


# Input
# Two (arrays, lists, tuples, or vectors) of unsigned integers.


# Output
# Boolean true or false as to whether or not the (list)s agree in terms of the orderings of their numbers.


# Enjoy!


def do_they_agree(alice, bob):
    position_in_bob = {num: idx for idx, num in enumerate(bob)}
    common_numbers = [num for num in alice if num in position_in_bob]
    for i in range(len(common_numbers) - 1):
        if position_in_bob[common_numbers[i]] > position_in_bob[common_numbers[i + 1]]:
            return False
    return True