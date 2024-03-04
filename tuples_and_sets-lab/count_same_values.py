numbers = tuple(map(float, input().split()))
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)
    else:
        continue

for num in unique:
    print(f"{num} - {numbers.count(num)} times")
