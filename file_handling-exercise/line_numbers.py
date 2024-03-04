import string

file = open("text.txt", "r")
result = {}
text = list(file)
counter = 0
output_list = []

for row in text:
    counter += 1
    alphas = 0
    symbols = 0

    for x in row:
        if x != " ":
            if x.isalpha():
                alphas += 1

            elif x in string.punctuation:
                symbols += 1

    key = f"Line {counter}: " + row[:-1]
    result[key] = [alphas, symbols]

for key, value in result.items():
    output_list.append(f"{key} ({value[0]}) ({value[1]})")

output = open("output.txt", "w")
for x in output_list:
    output.writelines(f"{x}\n")

output.close()
