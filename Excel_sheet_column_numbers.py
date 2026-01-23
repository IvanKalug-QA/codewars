# Write a function that, given a column title as it appears in an Excel sheet, returns its corresponding column number.

# All column titles will be uppercase.

# Examples:

# Column title: "A" --> return 1
# Column title: "Z" --> return 26
# Column title: "AA" --> return 27

def title_to_number(title):
    result = 0
    for char in title:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result