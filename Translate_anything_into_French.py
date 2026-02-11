# Sacrebleu!

# French can be pretty hard to master, and it might take you quite a while if you want to learn it from scratch...

# Fortunately, we come to the rescue with this kata, and you will soon be able to translate anything into French.

# French often use the words "Baguette" (in reference to their marvelous bread: https://en.wikipedia.org/wiki/Baguette). Moreover, they like to shout "Encore, encore!" at the end of an accordeon concert. Here we will shout "Encore!" at the end of our sentence.

# In this kata, our i_speak_french method will translate any sentence argument into its French translation :

# Every word from the sentence must be translated into "Baguette" (if it is the begining of the sentence), or "baguette" otherwise.

# Every sentence must end by an "Encore!" exclamation. A sentence is ended by a final dot ("."), or by the end of the string argument.

# You will expect a string as argument, no non-alphabetical values will be used.


def i_speak_french(sentence):
    if not sentence:
        return sentence
    sentence = sentence.strip()
    if not sentence:
        return "Encore!"
    
    result = []
    current_sentence = []
    
    for i, char in enumerate(sentence):
        if char == '.':
            if current_sentence:
                processed = process_sentence_words(current_sentence)
                result.append(processed + " Encore!")
                current_sentence = []
            else:
                result.append("Encore!")
        else:
            current_sentence.append(char)
    
    if current_sentence:
        processed = process_sentence_words(current_sentence)
        result.append(processed + " Encore!")
    
    return ' '.join(result)

def process_sentence_words(word_list):
    text = ''.join(word_list)
    
    words = text.split()
    
    if not words:
        return ""
    
    processed_words = ["Baguette"]
    
    for _ in range(1, len(words)):
        processed_words.append("baguette")
    
    return ' '.join(processed_words)