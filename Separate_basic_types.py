# Given: a sequence of different type of values (number, string, boolean). You should return an object with a separate properties for each of types presented in input. Each property should contain an array of corresponding values.
#
# keep order of values like in input array
# if type is not presented in input, no corresponding property are expected
# So, for this input:
#
# ['a', 1, 2, False, 'b']
# expected output is:
#
# {
#   int: [1, 2],
#   str: ['a', 'b'],
#   bool: [False]
# }

from collections import defaultdict
def separate_types(seq):
    types = {}
    for i in seq:
        if isinstance(i, bool):
            if bool not in types:
                 types[bool] = [i]
            else:
                types[bool].append(i)
        elif isinstance(i, int):
            if int not in types:
                types[int] = [i]
            else:
                types[int].append(i)
        elif isinstance(i, str):
            if str not in types:
                types[str] = [i]
            else:
                types[str].append(i)
    return types