from math import log


def log_func(num, base):
    if base == "natural":
        return f"{log(num):.2f}"
    else:
        return f"{log(num, int(base)):.2f}"


number = int(input())
log_base = input()
print(log_func(number, log_base))
