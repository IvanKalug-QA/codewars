# n this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.
#
# The first element of the array is at index 0.
#
# Good luck!

def total(arr):
    def is_prime(num):
        prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
        i = 5;
        d = 2;

        while prime and i * i <= num:
            prime = num % i != 0
            i += d
            d = 6 - d # чередование прироста 2 и 4: 5 + 2, 7 + 4, 11 + 2, и т.д.
        return prime
    count = 0
    for i in range(len(arr)):
        if is_prime(i):
            count += arr[i]
    return count