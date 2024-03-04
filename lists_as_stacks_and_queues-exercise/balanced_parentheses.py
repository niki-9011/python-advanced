sequence_of_parentheses = input()
opening_brackets = []

pairs = {
    "{": "}",
    "[": "]",
    "(": ")"}

balance = True


for char in sequence_of_parentheses:
    if char in "({[":
        opening_brackets.append(char)
    elif char in ")}]":
        if opening_brackets:
            element = opening_brackets[-1]
            if pairs[element] == char:
                opening_brackets.pop()
            else:
                balance = False
                break
        else:
            balance = False
            break

if balance :
    print("YES")
else:
    print("NO")
