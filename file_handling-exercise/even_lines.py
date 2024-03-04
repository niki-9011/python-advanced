symbols = ["-", ",", ".", "!", "?"]
file = open("text.txt", "r")

text = list(file)
output = []

for x in range(len(text)):
    if x % 2 == 0:
        for symbol in text[x]:
            if symbol in symbols:
                text[x] = text[x].replace(symbol, "@")

        output.append(" ".join(text[x][:-1].split()[::-1]))

file.close()

print(*output, sep="\n")
