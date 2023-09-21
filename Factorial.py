# DESCRIPTION:
# Your task is to write function factorial.

def factorial(n):
    num = n
    if n == 0:
        return 1
    for i in range(1,n):
        num *= i
    return num