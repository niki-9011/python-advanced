def list_manipulator(some_list, command, side, *args):
    if command == 'remove':
        quantity = args[0] if args else 1
        if side == 'end':
            some_list = some_list[:-quantity]
        elif side == 'beginning':
            some_list = some_list[quantity:]
    elif command == 'add':
        some_list = some_list + list(args) if side == 'end' else list(args) + some_list
    return some_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))