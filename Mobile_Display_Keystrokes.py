# Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?
# Well, here you have to calculate how many keystrokes you have to do for a specific word.
#
# This is the layout:
#
#
# Given a string, return the number of keystrokes necessary to type it. You can assume that the input will entirely consist of characters included in the mobile layout (lowercase letters, digits, and the symbols * and #).
#
# Examples
# "*#"       =>  2 (1 + 1)
# "123"      =>  3 (1 + 1 + 1)
# "abc"      =>  9 (2 + 3 + 4)
# "codewars" => 26 (4 + 4 + 2 + 3 + 2 + 2 + 4 + 5)

def mobile_keyboard(s):
    buttons = ['0', '1', '2abc', '3def', '4ghi', '5jkl', '6mno', '7pqrs', '8tuv', '9wxyz', '*', '#']
    click = 0
    for i in s:
        for j in buttons:
            if i in j:
                click += (j.index(i) + 1)
                break
    return click