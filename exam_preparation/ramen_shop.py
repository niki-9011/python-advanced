from collections import deque

ramens = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while customers:
    if not ramens:
        print("Out of ramen! You didn't manage to serve all customers.")
        break

    else:
        customer = customers.popleft()
        ramen = ramens.pop()

        if customer > ramen:
            customers.appendleft(customer - ramen)

        elif customer < ramen:
            ramens.append(ramen - customer)
else:
    print("Great job! You served all the customers.")

if customers:
    print(f"Customers left: {', '.join([str(x) for x in customers])}")

if ramens:
    print(f"Bowls of ramen left: {', '.join([str(z) for z in ramens])}")
