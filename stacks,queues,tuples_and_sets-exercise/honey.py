import sys
from io import StringIO
from collections import deque

test_input1 = '''20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /
'''
test_input2 = '''30
15 9 5 150 8
* + + * -
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

bees = deque([int(x) for x in input().split()])
nectar_stack = [int(n) for n in input().split()]
operators = deque(input().split())

honey = 0

symbols = {"+": lambda a, b: a + b,
           "-": lambda a, b: a - b,
           "*": lambda a, b: a * b,
           "/": lambda a, b: a / b}

while bees and nectar_stack:

    bee = bees.popleft()
    nectar = nectar_stack.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = operators.popleft()
    honey += abs(symbols[operator](bee, nectar))

print(f"Total honey made: {honey}")

if nectar_stack:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_stack])}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
