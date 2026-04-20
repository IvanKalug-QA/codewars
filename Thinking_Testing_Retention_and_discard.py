# No Story

# No Description

# Only by Thinking and Testing

# Look at the results of the testcases, and guess the code!

def mystery(n):
    if n < 1:
        return []
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 1:
                result.append(i)
            j = n // i
            if j != i and j % 2 == 1:
                result.append(j)
    return sorted(result)