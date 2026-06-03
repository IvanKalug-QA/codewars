# Farmer Bob has a big farm where he grows chickens, rabbits, and cows. It is very difficult to count the number of animals for each type manually, so he decided to buy a system to do it. However, he bought a cheap system that can only count the total number of heads, legs, and horns of the animals on the farm. Can you help Bob figure out how many chickens, rabbits, and cows he has?

# All chickens have 2 legs, 1 head and no horns; all rabbits have 4 legs, 1 head and no horns; all cows have 4 legs, 1 head and 2 horns.

# Your task is to write a function

# get_animals_count(legs_number, heads_number, horns_number)
# which returns a dictionary

# {"rabbits" : rabbits_count, "chickens" : chickens_count, "cows" : cows_count}
# Parameters legs_number, heads_number, horns_number are integers, all tests have valid input.

# Example:

# get_animals_count(34, 11, 6); # Should return {"rabbits" : 3, "chickens" : 5, "cows" : 3}
# get_animals_count(154, 42, 10); # Should return {"rabbits" : 30, "chickens" : 7, "cows" : 5}

def get_animals_count(legs_number, heads_number, horns_number):
    cows = horns_number // 2
    
    remaining_heads = heads_number - cows
    remaining_legs = legs_number - (cows * 4)
    
    rabbits = (remaining_legs - 2 * remaining_heads) // 2
    chickens = remaining_heads - rabbits
    
    return {"rabbits": rabbits, "chickens": chickens, "cows": cows}