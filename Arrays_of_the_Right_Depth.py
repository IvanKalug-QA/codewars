# Arrays of the Right Depth
# You are given a main array (a list of lists) and a dictionary of depth constraints. Each subarray in the main array can either be empty ([]) or contain only one nested array—nothing else.

# Task:

# Your goal is to verify whether all arrays inside the main array adhere to the given depth constraints.

# Understanding Depth

# The depth is zero-based:

# The elements in the main array have depth 1.
# A single nested empty array ([[]]) has depth 2.
# A double-nested empty array ([[[]]]) has depth 3, and so on.
# The depth constraints do not apply to the main array itself, only to the subarrays inside it.
# Constraints Dictionary

# The dictionary keys represent valid depths.
# The corresponding values indicate the maximum number of arrays at that depth that can appear in the main array.
# If the dictionary is empty, then there are no valid depths (meaning the result should be False).
# If an array has a depth not listed in the dictionary, return False.
# If there are more arrays of a certain depth than allowed, return False.
# If all constraints are met, return True.
# Examples:
# [[[]]], {2:1} -> True

# Explanation: The only element in the main array ([ [[]] ]) is an array with a single empty array inside it. This means it has depth 2, which is allowed once ({2:1}).

# [[[]], [[]]], {2:1} -> False

# Explanation: There are two arrays with depth 2, but only 1 is allowed.

# [ [[]], [], [[[]]], [], [[]] ], {2:6,1:2,3:1} -> True

# Explanation:

# Depth 1: There are two empty arrays ([]), and {1:2} allows them.
# Depth 2: There are three [[]], and {2:6} allows up to 6.
# Depth 3: There is one [[[]]], and {3:1} allows 1.
# No other depths appear, and all constraints are satisfied.
# [ [[]], [], [[[]]], [], [[]] ], {2:1,1:2,3:1}  -> False

# [ [[]], [], [[[]]], [], [[]] ], {2:6,1:2} -> False

# [ [[]], [], [[[]]], [], [[]] ], {} -> False

# [ [[]], [] ], {2:6,1:2,3:1,10:8,5:1,6:4} -> True

# [ [] ], {1:1} -> True

# [ [] ], {} -> False

def right_depth(arr, constraints):
    if not constraints:
        return False
    depth_counts = {}
    for element in arr:
        depth = 1
        current = element
        while isinstance(current, list) and len(current) == 1:
            current = current[0]
            depth += 1
        if not (isinstance(current, list) and len(current) == 0):
            return False
        if depth not in constraints:
            return False
        depth_counts[depth] = depth_counts.get(depth, 0) + 1
        if depth_counts[depth] > constraints[depth]:
            return False
    return True