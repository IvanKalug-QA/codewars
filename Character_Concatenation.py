# Given a string, you progressively need to concatenate the first character from the left and the first character from the right and "1", then the second character from the left and the second character from the right and "2", and so on.
#
# If the string's length is odd drop the central element.
#
# For example:
#
# "abcdef"  --> "af1be2cd3"
# "abc!def" --> "af1be2cd3" // same result

def char_concat(word):
    counter = 1
    result = []
    s = 0
    end = len(word) - 1
    while s < end:
        result.append(word[s])
        result.append(word[end])
        result.append(str(counter))
        s += 1
        end -= 1
        counter += 1
    return "".join(result)