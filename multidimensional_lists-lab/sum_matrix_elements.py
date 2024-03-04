numbers = input().split(", ")

matrix = []
row = int(numbers[0])
the_sum = 0

for n in range(row):
    columns = [int(x) for x in input().split(", ")]
    the_sum += sum(columns)
    matrix.append(columns)

print(the_sum)
print(matrix)

# n = [int(x) for x in input().split(", ")]
#
# matrix = []
# sum_of_numbers = 0
#
# for row in range(n[0]):
#     matrix.append([int(x) for x in input().split(", ")])
#
# sum_of_numbers = sum(sum(x) for x in matrix)
#
# print(sum_of_numbers)
# print(matrix)
