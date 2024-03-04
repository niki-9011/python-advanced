def concatenate(*args, **kwargs):
    text = "".join(args)

    for key, value in kwargs.items():
        text = text.replace(key, value)

    return text


# def concatenate(*args, **kwargs):
#     result = ""
#     for x in args:
#         result += x
#
#     for z in kwargs:
#         result = result.replace(z, kwargs[z])
#
#     return result

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
