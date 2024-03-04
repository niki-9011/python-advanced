numbers= int(input())

names = set()

for _ in range(numbers):
    current_name = input()
    names.add(current_name)

for name in names:
    print(name)
