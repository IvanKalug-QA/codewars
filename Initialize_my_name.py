# Some people just have a first name; some people have first and last names and some people have first, middle and last names.
#
# You task is to initialize the middle names (if there is any).
#
# Examples
# 'Jack Ryan'                   => 'Jack Ryan'
# 'Lois Mary Lane'              => 'Lois M. Lane'
# 'Dimitri'                     => 'Dimitri'
# 'Alice Betty Catherine Davis' => 'Alice B. C. Davis'

def initialize_names(name):
    l = list()
    name = name.split()
    l.append(name[0])
    if len(name) == 1:
        return name[0]
    for i in name[1:-1]:
        l.append(i[0] + '.')
    l.append(name[-1])
    return ' '.join(l)