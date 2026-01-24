# Return the lyrics of the nursery rhyme "Five little monkeys" (see below).

# But even monkeys can copy-paste, so you have to be smarter and make it short, because your code can be maximum 450 bytes long! (The original text is 800 bytes)

# Hint: use loops and variables for repeated text, or any other way to reduce your code size.

# Happy coding!

# Five little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!

# Four little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!

# Three little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!

# Two little monkeys jumping on the bed,
# One fell off and bumped his head.
# Mother called the doctor and the doctor said:
# No more monkeys jumping on the bed!

# One little monkey jumping on the bed,
# He fell off and bumped his head.
# Mother called the doctor and the doctor said:
# Put those monkeys right to bed!

def monkeys():
    w=['Five','Four','Three','Two','One']
    r=''
    for i in range(5):
        n=5-i
        s='little monkeys'if n>1 else'little monkey'
        r+=f'{w[i]} {s} jumping on the bed,\n'
        r+='He'if n==1 else'One'
        r+=' fell off and bumped his head.\nMother called the doctor and the doctor said:\n'
        r+='Put those monkeys right to bed!'if n==1 else'No more monkeys jumping on the bed!\n\n'
    return r