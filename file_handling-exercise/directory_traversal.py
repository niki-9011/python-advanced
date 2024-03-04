import os


def save_extension(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file):
            save_extension(file, first_level=True)


directory = input()

extensions = {}
result = []

save_extension(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for keys, values in extensions:
    result.append(f".{keys}")

    for file_name in sorted(values):
        result.append(f"- - -{file_name}")

print(*result, sep="\n")
