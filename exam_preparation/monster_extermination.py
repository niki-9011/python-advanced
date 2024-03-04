from collections import deque

enemy_armor = deque([int(x) for x in input().split(',')])
player_strikes = [int(x) for x in input().split(',')]

defeated_enemy = 0

while player_strikes and enemy_armor:
    curr_strike = player_strikes.pop()
    curr_armor = enemy_armor.popleft()

    if curr_strike >= curr_armor:
        defeated_enemy += 1
        curr_strike -= curr_armor

        if player_strikes:
            player_strikes[-1] += curr_strike
        if not player_strikes and curr_strike > 0:
            player_strikes.append(curr_strike)

    else:
        curr_armor -= curr_strike
        enemy_armor.append(curr_armor)

if not enemy_armor:
    print("All monsters have been killed!")
if not player_strikes:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {defeated_enemy}")
