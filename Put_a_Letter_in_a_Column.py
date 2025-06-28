# Create a function that takes index [0, 8] and a character. It returns a string with columns. Put character in column marked with index.
#
# Ex.: index = 2, character = 'B'
#
# | | |B| | | | | | |
#  0 1 2 3 4 5 6 7 8
# Assume that argument index is integer [0, 8]. Assume that argument character is string with one character.

def build_row_text(index, character):
    return {
        0: f"|{character}| | | | | | | | |", 1: f"| |{character}| | | | | | | |",
        2: f"| | |{character}| | | | | | |", 3: f"| | | |{character}| | | | | |",
        4: f"| | | | |{character}| | | | |", 5: f"| | | | | |{character}| | | |",
        6: f"| | | | | | |{character}| | |", 7: f"| | | | | | | |{character}| |",
        8: f"| | | | | | | | |{character}|"
    }[index]

