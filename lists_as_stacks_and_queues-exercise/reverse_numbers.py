stack = [x for x in input().split()]
result = [stack.pop() for _ in range(len(stack))]
print(*result)
#
# stack = input().split()
#
# result = ""
#
# for _ in range(len(stack)):
#     if stack:
#         result += stack.pop() + " "
# print("".join(result))