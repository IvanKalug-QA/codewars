# Bob is a theoretical coder - he doesn't write code, but comes up with theories, formulas and algorithm ideas. You are his secretary, and he has tasked you with writing the code for his newest project - a method for making the short form of a word. Write a function shortForm(C# ShortForm, Python short_form) that takes a string and returns it converted into short form using the rule: Remove all vowels, except for those that are the first or last letter. Do not count 'y' as a vowel, and ignore case. Also note, the string given will not have any spaces; only one word, and only Roman letters.
# Example:
#
# shortForm("assault");
# short_form("assault")
# ShortForm("assault");
# // should return "asslt"

def short_form(s):
    vowel = {"a", "e", "i", "o", "u"}
    result = [s[0]]
    for i in range(1, len(s) - 1):
        if s[i].lower() not in vowel:
            result.append(s[i])
    result.append(s[-1])
    return "".join(result)