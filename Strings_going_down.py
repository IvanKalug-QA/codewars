# Words Down the Page
# We normally read a list of words left to right:

# hi world yo
# Your job is to print them top to bottom instead.

# Each word becomes a column exactly one character wide, running down the page. The columns keep their original order, sit side by side, and are separated by a single space.

# Example
# vertical(["hi", "world", "yo"])
# returns the string

# h w y
# i o o
#   r
#   l
#   d
# hi and yo run out after two characters, so their columns simply go blank — but world keeps going, and it has to stay in the same column it started in.

# Rules
# Return a single string. Rows are joined with "\n". There is no trailing newline.
# The number of rows is the length of the longest word.
# Where a word has run out of characters, its cell is blank. The columns to the right must still line up.
# Every line is right-trimmed.
# An empty word "" still owns a column.
# An empty list returns "".
# Guarantees
# The input is a list of strings.
# No word contains a space.
# Words are made of letters (either case) and digits.

def vertical(words):
    if not words:
        return ""
    
    max_len = max(len(word) for word in words)
    result = []
    
    for i in range(max_len):
        line = ""
        for word in words:
            if i < len(word):
                line += word[i]
            else:
                line += " "
            line += " "
        result.append(line.rstrip())
    
    return "\n".join(result)