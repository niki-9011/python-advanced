from collections import deque

quantity_food = int(input())

orders = deque(map(int, input().split()))
result = ""
flag = False
flag2 = False
max_order = 0

if orders:
    max_order = max(orders)
while True:
    if len(orders) < 1:
        flag = True
        break

    if quantity_food >= orders[0]:
        quantity_food -= orders[0]
        orders.popleft()

    else:
        flag2 = True
        break

print(max_order)
if flag:
    print("Orders complete")
if flag2:
    for _ in range(len(orders)):
        result += str(orders.popleft()) + " "
    print(f"Orders left: {result}")

# from collections import deque
#
# food = int(input())
# each_order = deque(int(x)for x in input().split())
#
# max_order = max(each_order)
#
# while food > 0 or len(each_order) != 0:
#     if each_order:
#         order = each_order.popleft()
#         if food >= order:
#             food -= order
#         else:
#             each_order.appendleft(order)
#             break
#     else:
#         break
#
# print(max_order)
# if not each_order:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join([str(x) for x in each_order])}")