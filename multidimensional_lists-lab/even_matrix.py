n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append([z for z in row if z % 2 == 0])

print(matrix)
