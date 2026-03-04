# *** Nova polynomial derivative***

# This kata is from a series on polynomial handling. ( #1 #2 #3 #4)

# Consider a polynomial in a list where each element in the list element corresponds to the factors. The factor order is the position in the list. The first element is the zero order factor (the constant).

# p = [a0, a1, a2, a3] signifies the polynomial a0 + a1x + a2x^2 + a3*x^3

# In this kata return the derivative of a polynomial:

# [1, 2]    --> [2]
# [9, 1, 3] --> [1, 6]

def poly_derivative(p):
    if len(p) <= 1:
        return []
    return [i * p[i] for i in range(1, len(p))]