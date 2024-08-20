# Modify the kebabize function so that it converts a camel case string into a kebab case.
#
# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"
# Notes:
#
# the returned string should only contain lowercase letters

def kebabize(st):
    l = list()
    res = ''
    for i in st:
        if i.isalpha():
            if i.isupper():
                if len(res) >= 1:
                    l.append(res.lower())
                res = i
            else:
                res += i
    l.append(res.lower())
    return '-'.join(l)