# Your task is very simple. Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.
#
# For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].
#
# Goodluck :)

def case_sensitive(s):
    return [all(i.islower() for i in s), [i for i in s if i.isupper()]]