# Will My Horse Make It to the End?

# You are a professional horse rider and you are about to have a ride on a horse over the line of obstacles. You have a very experienced eye and you can instantly give a rough estimate of the hourse stamina. Moreover, you learned how much stamina it would take for a hourse to jump over a certain obstacle. The only problem now is to understand immediately if the given horse will actually overcome all of the obstacles before it runs out of energy! Your task is to help the horse rider to find it out.

# Task:
# Given the horse’s stamina and a map representing the course, determine if the horse can reach the end without running out of energy.

# Return True if the horse completes the course with stamina ≥ 0, otherwise return False.

# Input:
# stamina (integer) – the horse’s starting stamina.

# map (array of 0s and 1s) – represents the track:

# 0 – flat ground (no stamina loss).
# 1 – obstacle (requires stamina to jump).
# Stamina Cost per Obstacle:
# A single 1 (length 1) costs 2 stamina.

# A pair of consecutive 1s (length 2) costs 5 stamina.

# A triplet of consecutive 1s (length 3) costs 10 stamina.

# Examples:
# [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 18 -> False

# [1, 1], 5 -> True

# [0, 1, 0, 0, 0, 0, 1], 3 -> False

def estimator(obstacles, stamina):
    i = 0
    n = len(obstacles)
    
    while i < n:
        if obstacles[i] == 0:
            i += 1
            continue
        count = 0
        while i < n and obstacles[i] == 1:
            count += 1
            i += 1
        if count == 1:
            stamina -= 2
        elif count == 2:
            stamina -= 5
        elif count >= 3:
            stamina -= 10
        if stamina < 0:
            return False
    
    return True