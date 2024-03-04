number = int(input())

guests = set()
guests_not_come = set()

for num in range(number):
    guest = input()
    guests.add(guest)

command = input()
while command != "END":
    guests_not_come.add(command)
    command = input()

guests_come =  guests.difference(guests_not_come)

print(len(guests_come))

for comes in sorted(guests_come):
    print(comes)
