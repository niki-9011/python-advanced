text = input()

simbols = {}

for char in text:
    if char not in simbols:
        simbols[char] = 1
    else:
        simbols[char] += 1

print('\n'.join([f"{element}: {counter} time/s" for element, counter in sorted(simbols.items())]))

# text = tuple(x for x in input())
# simbols = {}
#
# for x in text:
#    if x not in simbols:
#        simbols[x] = text.count(x)
#
# print('\n'.join([f"{element}: {counter} time/s" for element, counter in sorted(simbols.items())]))
