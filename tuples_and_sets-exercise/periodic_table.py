numbers = int(input())

unique_elements = set()

for _ in range(numbers):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

print("\n".join([el for el in unique_elements]))
