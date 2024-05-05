# Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischievous hacker that has set out to sabotage all his good code.
#
# Your job is to take PEP8 compatible function names and convert them to camelCase. For example:
#
# zebulansNightmare('camel_case') == 'camelCase'
# zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
# zebulansNightmare('get_string') == 'getString'
# zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
# zebulansNightmare('main') == 'main'

def zebulans_nightmare(function):
    function = function.split('_')
    l = [function[0]]
    for i in function[1:]:
        l.append(i.capitalize())
    return ''.join(l)