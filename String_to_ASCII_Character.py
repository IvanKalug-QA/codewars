# You are given a string. Your job is to convert that string to upper case, then find the sum of each character converted to its ASCII value, then divide the sum by the string's length and round it down then convert that to its equivalent character in ASCII.
#
# Note: do it in maximum 57 characters
#
# Examples
# "abc"  -->  "B"
# "asd"  -->  "H"
# "iamareallyreallylongstringthatiscompletelyworthlessandisheretostophardcoders"  -->  "L"

solution=lambda s:chr(sum(map(ord,s.upper()))//len(s))