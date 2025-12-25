# A commutator is a type of algorithm that takes this form:

# A
# B
# A backwards
# B backwards
# These types of algorithms are very useful when solving the Rubik's Cube, so I need you to code a function that creates them.

# Rubik's cube notation is thus:

# Each side of the cube has a corresponding letter: R, L, U, D, F, B.
# Each letter has 3 variations:
# R: Turn the side 90 degrees clockwise.
# R': Turn the side 90 degrees counterclockwise.
# R2: Turn the side 180 degrees. (Note that R2' is not a valid turn.)
# Your function must take in 2 strings (A and B) with turns separated by spaces, and it must output a string of the same format with the completed commutator in full. (e.g., do not shorten the output as in Aza_rt's kata)

# Example:

# A: "R U"
# B: "F' L2"
# Result: "R U F' L2 U' R' L2 F"
# Note: When reversing a sequence, you must reverse the direction of the turns as well as the order.

def invert_move(move: str) -> str:
    if move.endswith("'"):
        return move[:-1]
    elif move.endswith("2"):
        return move
    else:
        return move + "'"

def create_commutator(a: str, b: str) -> str:
    moves_a = a.split()
    moves_b = b.split()
    
    reversed_a = []
    for move in reversed(moves_a):
        reversed_a.append(invert_move(move))
    
    reversed_b = []
    for move in reversed(moves_b):
        reversed_b.append(invert_move(move))
    
    result_parts = moves_a + moves_b + reversed_a + reversed_b
    return " ".join(result_parts)