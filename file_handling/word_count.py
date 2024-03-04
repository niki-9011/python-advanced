file_words = open("words.txt", "r")
text = open("input.txt", "r")

data = ""

for x in text:
    data += x.lower()


results = {}


for word in file_words:

    for x in word.split():
        if x in data:
            if x not in results:
                results[x] = data.count(x)
            else:
                results[x] += data.count(x)

print([f"{key} - {value}" for key, value in results.items()])
