# I will give you two strings. I want you to transform stringOne into stringTwo one letter at a time.

# Example:

# stringOne = 'bubble gum';
# stringTwo = 'turtle ham';

# Result:
# bubble gum
# tubble gum
# turble gum
# turtle gum
# turtle hum
# turtle ham

def mutate_my_strings(s1,s2):
    result = []
    s = [i for i in s1]
    result.append(''.join(s))
    for i in range(len(s1)):
        if s[i] != s2[i]:
            s[i] = s2[i]
            result.append(''.join(s))
    return '\n'.join(result) + '\n'