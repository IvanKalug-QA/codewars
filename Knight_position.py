# Description
# Write a function that accepts the current position of a knight in a chess board, it returns the possible positions that it will end up after 1 move. The resulted should be sorted.
#
# Example
# "a1" -> ["b3", "c2"]

def possible_positions(position):
    col_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    rev_col_map = {v: k for k, v in col_map.items()}
    current_col = col_map[position[0]]
    current_row = int(position[1])
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    possible_moves = []
    for col_delta, row_delta in moves:
        new_col = current_col + col_delta
        new_row = current_row + row_delta
        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            new_position = rev_col_map[new_col] + str(new_row)
            possible_moves.append(new_position)

    possible_moves.sort()
    return possible_moves