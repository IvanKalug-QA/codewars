# Your job is to create a calculator which evaluates expressions in Reverse Polish notation.
#
# For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.
#
# For your convenience, the input is formatted such that a space is provided between every token.
#
# Empty expression should evaluate to 0.
#
# Valid operations are +, -, *, /.
#
# You may assume that there won't be exceptional situations (like stack underflow or division by zero).

def calc(expr):
    stack = []
    for i in expr.split():
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '-':
            operand1, operand2 = stack.pop(), stack.pop()
            stack.append(operand2 - operand1)
        elif i == '/':
            operand1, operand2 = stack.pop(), stack.pop()
            stack.append(operand2 // operand1)
        else:
            if '.' in i:
                stack.append(float(i))
            else:
                stack.append(int(i))
    return stack.pop() if stack else 0