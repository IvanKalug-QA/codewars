# For "x", determine how many positive integers less than or equal to "x" are odd but not prime. Assume "x" is an integer between 1 and 10000.

# Example: 5 has three odd numbers (1,3,5) and only the number 1 is not prime, so the answer is 1

# Example: 10 has five odd numbers (1,3,5,7,9) and only 1 and 9 are not prime, so the answer is 2

def odd_not_prime(n):
    return sum(1 for i in range(1, n+1, 2) if i != 2 and (i < 2 or any(i % d == 0 for d in range(2, int(i**0.5)+1)) or i == 1))