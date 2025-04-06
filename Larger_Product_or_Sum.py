# Description
# For this Kata you will be given an array of numbers and another number n. You have to find the sum of the n largest numbers of the array and the product of the n smallest numbers of the array, and compare the two.
#
# If the sum of the n largest numbers is higher, return "sum"
# If the product of the n smallest numbers is higher, return "product"
# If the 2 values are equal, return "same"
#
# Note The array will never be empty and n will always be smaller than the length of the array.
#
# Example
# sum_or_product([10, 41, 8, 16, 20, 36, 9, 13, 20], 3) # => "product"
# Explanation
# The sum of the 3 highest numbers is 41 + 36 + 20 = 97
#
# The product of the lowest 3 numbers is 8 x 9 x 10 = 720
#
# The product of the 3 lowest numbers is higher than the sum of the 3 highest numbers so the function returns "product"

def sum_or_product(array, n):
    array.sort()
    max_sum = sum(array[-n:])
    min_mul = 1
    counter = 0
    for i in range(len(array)):
        if counter == n:
            break
        else:
            min_mul *= array[i]
            counter += 1
    return 'sum' if max_sum > min_mul else 'product' if min_mul > max_sum else 'same'