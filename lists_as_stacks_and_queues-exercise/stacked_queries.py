n = int(input())

stack = []

for _ in range(n):
    query = input().split()

    if int(query[0]) == 1:
        stack.append(int(query[1]))
    elif int(query[0]) == 2:
        if stack:
            stack.pop()
    elif int(query[0]) == 3:
        if stack:
            print(max(stack))
    elif int(query[0]) == 4:
        if stack:
            print(min(stack))

print(*stack[::-1], sep =", ")