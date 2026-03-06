# In music, each note is named by its pitch class (e.g., C, E♭, F♯), and each pitch class can alternatively be expressed as an integer from 0 to 11. Your task will be to write a function that, when given a letter-based pitch class, returns the corresponding integer.

# Only seven letters are used to name the notes: "A" through "G." These letter names are cyclical, just like the days of the week. The notes corresponding to those letters are called the "natural notes." Here are the numbers corresponding to each of them:

# C : 0
# D : 2
# E : 4
# F : 5
# G : 7
# A : 9
# B : 11
# So 'D' has a pitch class of 2, and 'B' has a pitch class of 11.

# The sharp sign ("♯") is essentially an increment operator, so "C♯" (pronounced "C sharp") refers to one note higher than C, which has a value of 1, whereas F♯ has a value of 6. Since Codewars doesn't allow the sharp sign, we'll use a number sign ("#") instead.

# The flat sign ("♭") is the opposite of a sharp, meaning one note lower. F♭ has a value of 4, and C♭ has a value of 11 (going below 0 cycles back to 11, the twelve-note system is cyclical). Since Codewars doesn't allow the flat sign, we'll use a lowercase "b" instead.

# Return the appropriate null value in your language (JS: null, Python: None, Ruby: nil) for invalid input.

# (Next in this series: Integer to Musical Pitch Classes)

def pitch_class(note: str) -> int | None:
    base_values = {
        'C': 0,
        'D': 2,
        'E': 4,
        'F': 5,
        'G': 7,
        'A': 9,
        'B': 11
    }
    if not note or len(note) == 0:
        return None
    letter = note[0].upper()
    if letter not in base_values:
        return None
    value = base_values[letter]
    for modifier in note[1:]:
        if modifier == '#':
            value += 1
        elif modifier == 'b':
            value -= 1
        else:
            return None
    value %= 12
    return value