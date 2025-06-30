# Some but not all
# Description
# Your task is to create a function that given a sequence and a predicate, returns True if only some (but not all) the elements in the sequence are True after applying the predicate
#
# Examples
# ('abcdefg&%$', x -> isLetter(x)) == true
# ('&%$=', x -> isLetter x) == false
# ('abcdefg', x -> isLetter x) == false
#
# ([4, 1], x -> x > 3) == true
# ([1, 1], x -> x > 3) == false
# ([4, 4], x -> x > 3) == false

def some_but_not_all(seq, pred):
    if all(pred(i) for i in seq):
        return False
    return any(pred(i) for i in seq)