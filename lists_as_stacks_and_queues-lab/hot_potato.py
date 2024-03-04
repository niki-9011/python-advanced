from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    for x in range(1, n + 1):
        if x == n:
            print(f"Removed {kids.popleft()}")
        else:
            kid = kids.popleft()
            kids.append(kid)

print(F"Last is {''.join(kids)}")
