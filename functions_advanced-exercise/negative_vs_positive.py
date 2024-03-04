def sum_positive(numbers):
    positive = 0
    for x in numbers:
        if x > 0:
            positive += x
    return positive


def sum_negative(numbers):
    negative = 0
    for z in numbers:
        if z < 0:
            negative += z
    return negative


numbers = [int(x) for x in input().split()]

print(sum_negative(numbers))
print(sum_positive(numbers))

if abs(sum_positive(numbers)) < abs(sum_negative(numbers)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")


# def sum_negative(negative):
#     return sum(negative)
#
# def sum_positive(positive):
#     return sum(positive)
#
#
# positive_nums = []
# negative_nums = []
#
# numbers = [int(x) for x in input().split()]
#
# for x in numbers:
#     if x > 0:
#         positive_nums.append(x)
#     else:
#         negative_nums.append(x)
#
# print(sum_negative(numbers))
# print(sum_positive(numbers))

# if abs(sum_positive(numbers)) < abs(sum_negative(numbers)):
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")


