# Create a program that will return whether an input value is a str, int, float, or bool. Return the name of the value.
#
# Examples
# Input = 23 --> Output = int
# Input = 2.3 --> Output = float
# Input = "Hello" --> Output = str
# Input = True --> Output = bool

def types(x):
    if isinstance(x, bool):
        return "bool"
    elif isinstance(x, int):
        return "int"
    elif isinstance(x, float):
        return "float"
    else:
        return "str"