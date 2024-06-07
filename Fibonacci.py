# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    l = [0, 1]
    for i in range(n):
        l.append(l[-2] + l[-1])

    return l[n]