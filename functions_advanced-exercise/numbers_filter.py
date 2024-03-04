def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = [x for x in kwargs["odd"] if x % 2 != 0]

    if "even" in kwargs:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))


#
# def even_odd_filter(**kwargs):
#     result = {}
#     for key in kwargs:
#         if key == "even":
#             result[key] = []
#             for value in kwargs[key]:
#                 if value % 2 == 0:
#                     result[key].append(value)
#
#         elif key == "odd":
#             result[key] = []
#             for value in kwargs[key]:
#                 if value % 2 != 0:
#                     result[key].append(value)
#
#     return dict(sorted(result.items()))
#
#
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
#
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))


# def even_odd_filter(**kwargs):
#     result = {}
#
#     for key, value in kwargs.items():
#         party = 0 if key == "even" else 1
#         filtered = [x for x in value if x % 2 == party]
#         result[key] = filtered
#
#     return dict(sorted(result.items(), key=lambda x: -len(x[1])))


# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
#
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
