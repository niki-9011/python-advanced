def solve(inputs):
    message = inputs.pop(0)

    for line in inputs:
        if line == 'Buy':
            break

        command, *args = line.split('?')

        if command == 'TakeEven':
            message = ''.join(message[i] for i in range(len(message)) if i % 2 == 0)
            print(message)
        elif command == 'ChangeAll':
            arg1, arg2 = args
            message = message.replace(arg1, arg2)
            print(message)
        elif command == 'Reverse':
            arg1 = args[0]
            if arg1 in message:
                reversed_substring = arg1[::-1]
                message = message.replace(arg1, '', 1)
                message += reversed_substring
                print(message)
            else:
                print('error')

    print(f"The cryptocurrency is: {message}")


solve([
    "z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
    "TakeEven",
    "Reverse?!nzahc",
    "ChangeAll?m?g",
    "Reverse?adshk",
    "ChangeAll?z?i",
    "Buy"
])

solve([
    "PZDfA2PkAsakhnefZ7aZ",
    "TakeEven",
    "TakeEven",
    "TakeEven",
    "ChangeAll?Z?X",
    "ChangeAll?A?R",
    "Reverse?PRX",
    "Buy"
])
