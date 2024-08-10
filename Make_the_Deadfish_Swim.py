# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
#
# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    l = list()
    count = 0
    for i in data:
        match i:
            case 'o':
                l.append(count)
            case 'i':
                count += 1
            case 'd':
                count -= 1
            case 's':
                count = count ** 2
    return l