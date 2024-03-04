import operator as op

def mathematical_operations(first_number, operator , second_number):
    first_number, second_number = float(first_number), float(second_number)
    operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv, "^": op.xor}

    return operators[operator](first_number, second_number)