def operate(operator, *args):
    def add(*args):
        return sum(args)


    def subtract(z, *args):
        return z + sum(-y for y in args)


    def multiplay(i, *args):
        for j in args:
            i *= j
        return i

    def divaide(a, *args):
        for k in args:
            a /= k
        return a


    if operator == "+":
        return add(*args)
    elif operator == "-":
        return subtract(*args)
    elif operator == "*":
        return multiplay(*args)
    elif operator == "/":
        return divaide(*args)

print(operate("+", 1, 2, 3))
print(operate("-", 10, 5, 3))
print(operate("*", 3, 4))
print(operate("/", 100, 2, 5))

