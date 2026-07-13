# Reverse a message so that the words and letters passed into it are made lower case and reversed. In addition, capitalise the first letter of the newly reversed words. If a number or symbol(!#,>) is now in the first position of the word, no capitalisation needs to occur.

# Example:

# reverseMessage('This is an example of a Reversed Message!')
# Returns: '!egassem Desrever A Fo Elpmaxe Na Si Siht'

def reverse_message(text):
    reversed_text = text[::-1]
    words = reversed_text.split()
    result_words = []
    for word in words:
        word_lower = word.lower()
        if word_lower and word_lower[0].isalpha():
            word_capitalized = word_lower[0].upper() + word_lower[1:]
        else:
            word_capitalized = word_lower
        
        result_words.append(word_capitalized)
    return ' '.join(result_words)