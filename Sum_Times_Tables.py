# Write a function which sums the result of the sums of the elements specified in table multiplied by all the numbers in between min and max including themselves.
#
# For example, for table=[2,5], min=1, max=3 the result should be the same as
#
# 2*1 + 2*2 + 2*3 +
# 5*1 + 5*2 + 5*3
# i.e. the table of two from 1 to 3 plus the table of five from 1 to 3
#
# All the numbers are integers but you must take in account:
#
# table could be empty.
# min could be negative.
# max could be really big.
# It is guaranteed that the input min <= max

def sum_times_tables(table, a, b):
    s = 0
    for i in table:
        for j in range(a, b + 1):
            s += i * j
    return s