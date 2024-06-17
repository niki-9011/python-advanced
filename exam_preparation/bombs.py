from collections import deque

bomb_effects = deque(int(n) for n in input().split(','))
bomb_casing = [int(n) for n in input().split(',')]

bombs_names = {40: 'Datura Bombs',
               60: 'Cherry Bombs',
               120: 'Smoke Decoy Bombs'}
created_bombs = {'Datura Bombs': 0,
                 'Cherry Bombs': 0,
                 'Smoke Decoy Bombs': 0}

enough_bombs = False
while True:
    effect = bomb_effects.popleft()
    casing = bomb_casing.pop()
    value = effect + casing

    if value not in bombs_names:
        if value >= 45:
            while value not in bombs_names:
                effect -= 5
                value = effect + casing
                if value < min(bombs_names.keys()):
                    break
    if value in bombs_names:
        created_bombs[bombs_names[value]] += 1

    enough_bombs = created_bombs['Datura Bombs'] >= 3 \
                   and created_bombs['Cherry Bombs'] >= 3 \
                   and created_bombs['Smoke Decoy Bombs'] >= 3

    if enough_bombs or not bomb_effects or not bomb_casing:
        break

if enough_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
left_bombs_effects = 'empty' if not bomb_effects else ', '.join(map(str, bomb_effects))
print(f'Bomb Effects: {left_bombs_effects}')
left_bombs_casing = 'empty' if not bomb_casing else ', '.join(map(str, bomb_casing))
print(f'Bomb Casings: {left_bombs_casing}')
print('\n'.join(f'{name}: {count}' for name, count in sorted(created_bombs.items())))