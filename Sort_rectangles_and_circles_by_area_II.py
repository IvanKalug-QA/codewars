# In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
# Your task is to return a new sequence of dimensions, sorted ascending by area.
#
# For example,
#
# seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
# sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]
# This kata inspired by Sort rectangles and circles by area.


def sort_by_area(seq):
    def calculate_area(item):
        if isinstance(item, tuple):
            return item[0] * item[1]
        else:
            return 3.141592653589793 * item * item

    return sorted(seq, key=calculate_area)