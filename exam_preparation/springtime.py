def start_spring(**objects):
    data = {}

    for key, value in objects.items():
        if value not in data:
            data[value] = [key]
        else:
            data[value].append(key)

    output = ""

    for key, value in sorted(data.items(), key=lambda x: (-len(x[1]), x[0], x[1])):
        output += f"{key}:\n"

        for element in sorted(value):
            output += f"-{element}\n"

    return output


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
