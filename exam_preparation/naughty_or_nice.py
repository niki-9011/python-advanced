class KidList:

    def __init__(self, *data):
        self.kid_list = data[0]
        self.kids_dict = {"Nice": [], "Naughty": [], "Not found": []}


class SantaInAction:

    def __init__(self, data: KidList):
        self.data = data

    def kids_matches(self, check):
        return [t for t in self.data.kid_list if check in t]

    def santa_check_kids(self, *commands):
        for info in commands:
            number, command = info.split("-")

            kids = self.kids_matches(int(number))

            if len(kids) == 1:
                self.data.kids_dict[command].append(kids[0][1])
                self.data.kid_list.remove(kids[0])

    def check_keywords(self, **kwargs):
        for name, command in kwargs.items():

            kids = self.kids_matches(name)

            if len(kids) == 1:
                self.data.kids_dict[command].append(kids[0][1])
                self.data.kid_list.remove(kids[0])

    def check_for_not_found_kids(self):
        not_found_kids = [x[1] for x in self.data.kid_list]
        self.data.kids_dict["Not found"].extend(not_found_kids)


class Result:

    def __init__(self):
        self.result = []

    def prepare_result(self, data: KidList):
        for type_of_kid, kids in data.kids_dict.items():
            if kids:
                self.result.append(f"{type_of_kid}: {', '.join(kids)}")


def naughty_or_nice_list(*args, **kwargs):
    kid_list = KidList(*args)
    santa_in_action = SantaInAction(kid_list)
    santa_in_action.santa_check_kids(*args[1:])
    santa_in_action.check_keywords(**kwargs)
    santa_in_action.check_for_not_found_kids()
    result = Result()
    result.prepare_result(kid_list)
    return '\n'.join(result.result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
