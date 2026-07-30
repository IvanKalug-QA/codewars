# You are given an array of 6-faced dice. Each die is represented by its face up.

# Calculate the minimum number of rotations needed to make all faces the same.

# 1 will require one rotation to have 2, 3, 4 and 5 face up, but would require two rotations to make it the face 6, as 6 is the opposite side of 1.

# The opposite side of 2 is 5 and 3 is 4.

# Examples
# dice = {1, 1, 1, 1, 1, 6} --> 2:
# rotate 6 twice to get 1

# dice = {1, 2, 3} --> 2:
# 2 rotations are needed to make all faces either 1, 2, or 3

# dice = {3, 3, 3} --> 0:
# all faces are already identical

# dice = {1, 6, 2, 3} --> 3:
# rotate 1, 6 and 3 once to make them all 2

def count_min_rotations(dice):
    opposite = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    adjacent = {}
    for face in range(1, 7):
        opp = opposite[face]
        adj = [f for f in range(1, 7) if f != face and f != opp]
        adjacent[face] = adj
    
    min_rotations = float('inf')
    
    for target in range(1, 7):
        rotations = 0
        for die in dice:
            if die == target:
                continue
            elif die in adjacent[target]:
                rotations += 1
            else:
                rotations += 2
        min_rotations = min(min_rotations, rotations)
    
    return min_rotations