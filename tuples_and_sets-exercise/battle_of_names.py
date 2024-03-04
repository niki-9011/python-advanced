numbers = int(input())

odd = set()
even = set()
result = set()

for num in range(1, numbers + 1):
    suma_char_name = int(sum([ord(char) for char in input()]) / int(num))
    if suma_char_name % 2 == 0:
        odd.add(suma_char_name)
    else:
        even.add(suma_char_name)

if sum(odd) == sum(even):
    result = odd.union(even)

elif sum(odd) > sum(even):
    result = odd.union(even)

elif sum(odd) < sum(even):
    result = even.difference(odd)

print(", ".join([str(x) for x in result]))


# def print_func(odd, even):
#     result = set()
#     if sum(odd) == sum(even):
#         result = odd.union(even)
#
#     elif sum(odd) > sum(even):
#         result = odd.union(even)
#
#     elif sum(odd) < sum(even):
#         result = even.difference(odd)
#     print(*result, sep=", ")
#
#
# def ascii_sum(numbers):
#     ascii_sum = 0
#     even = set()
#     odd = set()
#     counter = 0
#     for _ in range(numbers):
#         name = input()
#         ascii_sum = 0
#
#         for x in name:
#             ascii_sum += ord(x)
#         counter += 1
#         ascii_sum = int(ascii_sum / counter)
#         if ascii_sum % 2 == 0:
#             odd.add(ascii_sum)
#         else:
#             even.add(ascii_sum)
#
#     print_func(odd, even)
#
#
# numbers = int(input())
# ascii_sum(numbers)