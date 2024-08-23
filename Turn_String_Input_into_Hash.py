# Please write a function that will take a string as input and return a hash. The string will be formatted as such. The key will always be a symbol and the value will always be an integer.
#
# "a=1, b=2, c=3, d=4"
# This string should return a hash that looks like
#
# { 'a': 1, 'b': 2, 'c': 3, 'd': 4}Please write a function that will take a string as input and return a hash. The string will be formatted as such. The key will always be a symbol and the value will always be an integer.
#
# "a=1, b=2, c=3, d=4"
# This string should return a hash that looks like
#
# { 'a': 1, 'b': 2, 'c': 3, 'd': 4}

def str_to_hash(st):
    d = dict()
    if not len(st):
        return d
    for i in st.split():
        word = i.split('=')
        d[word[0]] = int(word[-1][0:-1]) if ',' in word[-1] else int(word[-1])
    return d