# Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number. (A proper divisor of a number is a positive factor of that number other than the number itself. For example, the proper divisors of 6 are 1, 2, and 3.)

# For example, the smallest pair of amicable numbers is (220, 284); for the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; and the proper divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220.

# Derive a function which returns true/True if pair num1 num2 are amicable, false/False if not.

def amicable_numbers(n1, n2):
    if n1 == n2:
        return False
    
    def sum_of_proper_divisors(n):
        total = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                total += i
                if i != 1 and i != n // i:
                    total += n // i
        return total
    
    return sum_of_proper_divisors(n1) == n2 and sum_of_proper_divisors(n2) == n1