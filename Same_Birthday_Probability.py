# Given n number of people in a room, calculate the probability that any two people in that room have the same birthday (assume 365 days every year = ignore leap year). Answers should be two decimals unless whole (0 or 1) eg 0.05

def calculate_probability(n):
    if n <= 1:
        return 0.00
    if n > 365:
        return 1.00
    
    prob_no_match = 1.0
    for i in range(n):
        prob_no_match *= (365 - i) / 365
    
    prob_match = 1 - prob_no_match
    
    if prob_match == 0 or prob_match == 1:
        return round(prob_match, 2)
    
    return round(prob_match, 2)