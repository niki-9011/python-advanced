n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix += [v for v in row]

print(matrix)
