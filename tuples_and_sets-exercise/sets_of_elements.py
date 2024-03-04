n, m = input().split()

first = set()
second = set()

for _ in range(int(n)):
    number1 = int(input())
    first.add(number1)

for _ in range(int(m)):
    number2 = int(input())
    second.add(number2)

unique_elements = first.intersection(second)

for num in unique_elements:
    print(num)
