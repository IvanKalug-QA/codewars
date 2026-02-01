# We’ve all seen katas that ask for conversion from snake-case to camel-case, from camel-case to snake-case, or from camel-case to kebab-case — the possibilities are endless.

# But if we don’t know the case our inputs are in, these are not very helpful.

# Task:
# So the task here is to implement a function that takes a string and returns a string with the case the input is in. The possible case types are "kebab", "camel", and "snake". If none of the cases match with the input, or if there are no separators / case changes in the input, return "none". Inputs will only have letters (no numbers or special characters).

# Some definitions
# Kebab case: lowercase-words-separated-by-hyphens

# Camel case: lowercaseFirstWordFollowedByCapitalizedWords

# Snake case: lowercase_words_separated_by_underscores

# Examples:
# "hello-world" => "kebab"
# "hello-to-the-world" => "kebab"
# "helloWorld" => "camel"
# "helloToTheWorld" => "camel"
# "hello_world" => "snake"
# "hello_to_the_world" => "snake"
# "hello__world" => "none"
# "hello_World" => "none"
# "helloworld" => "none"
# "hello-World" => "none"

import re
def case_id(c_str):
    has_hyphen = '-' in c_str
    has_underscore = '_' in c_str
    if has_hyphen and has_underscore:
        return "none"
    has_upper = any(ch.isupper() for ch in c_str)
    if has_hyphen and not has_upper:
        parts = c_str.split('-')
        if all(part.isalpha() and part.islower() and part for part in parts):
            return "kebab"
        return "none"
    if has_underscore and not has_upper:
        parts = c_str.split('_')
        if all(part.isalpha() and part.islower() and part for part in parts):
            return "snake"
        return "none"
    
    if not has_hyphen and not has_underscore:
        if c_str[0].islower() and has_upper:
            if re.fullmatch(r'[a-z]+([A-Z][a-z]*)+', c_str):
                return "camel"
    
    return "none"