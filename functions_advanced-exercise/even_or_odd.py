def even_odd(*args):
    result = []
    command = args[-1]
    new = args[:-1]

    for x in new:
        if command == "even":
            if x % 2 == 0:
                result.append(x)
        elif command == "odd":
            if x % 2 != 0:
                result.append(x)

    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

#
# def even_odd(*args):
#     *args, command = args
#     result = []
#
#     def even_func(*args):
#
#         for x in args:
#             if x % 2 == 0:
#                 result.append(x)
#         return result
#
#
#     def odd_func(*args):
#
#         for x in args:
#             if x % 2 != 0:
#                 result.append(x)
#         return result
#
#
#     if command == "even":
#         return even_func(*args)
#     elif command == "odd":
#         return odd_func(*args)
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
