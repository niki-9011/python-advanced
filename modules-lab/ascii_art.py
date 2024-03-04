from pyfiglet import figlet_format


def art_func(txt):
    return f"{figlet_format(txt)}"


text = input()
print(art_func(text))
