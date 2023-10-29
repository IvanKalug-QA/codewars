# Write a program that outputs the top n elements from a list.
#
# Example:
#
# largest(2, [7,6,5,4,3,2,1])
# # => [6,7]

def largest(n, xs):
    l = []
    for i in range(n):
        n = max(xs)
        l += [n]
        xs.pop(xs.index(n))
    return sorted(l)