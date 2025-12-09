# In this Kata, you will be given directions and your task will be to find your way back.

# solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]) = ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
# solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr']) =  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']
# More examples in test cases.

# Good luck!

def solve(arr):
    dirs = []
    roads = []
    for step in arr:
        parts = step.split(" on ")
        dirs.append(parts[0])
        roads.append(parts[1])
    result = []
    result.append("Begin on " + roads[-1])
    for i in range(len(roads) - 1, 0, -1):
        original_dir = dirs[i] 
        
        if original_dir == "Left":
            new_dir = "Right"
        elif original_dir == "Right":
            new_dir = "Left"
        else:
            new_dir = "Begin"
        
        result.append(new_dir + " on " + roads[i-1])
    
    return result