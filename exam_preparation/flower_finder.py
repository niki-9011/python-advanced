from collections import deque

vowels = deque(x for x in input().split())
consonants_stack = [x for x in input().split()]

word = []
flag = False

rose = ["r", "o", "s", "e"]
rose1 = "rose"
tulip = ["t", "u", "l", "i", "p"]
tulip1 = "tulip"
lotus = ["l", "o,", "t", "u", "s"]
lotus1 = "lotus"
daffodil = ["d", "a", "f", "f", "o", "d", "i", "l"]
daffodil1 = "daffodil"

while vowels and consonants_stack:
    vowel = vowels.popleft()
    consonant = consonants_stack.pop()

    if vowel in rose or vowel in tulip or vowel in lotus or vowel in daffodil:
        if vowel in rose:
            rose.remove(vowel)
        if vowel in tulip:
            tulip.remove(vowel)
        if vowel in lotus:
            lotus.remove(vowel)
        if vowel in daffodil:
            daffodil.remove(vowel)

    if consonant in rose or consonant in tulip or consonant in lotus or consonant in daffodil:
        word.append(consonant)
        if consonant in rose:
            rose.remove(consonant)
        if consonant in tulip:
            tulip.remove(consonant)
        if consonant in lotus:
            lotus.remove(consonant)
        if consonant in daffodil:
            daffodil.remove(consonant)

    if not rose:
        word = rose1
        flag = True
        break
    if not tulip:
        word = tulip1
        flag = True
        break
    if not lotus:
        word = lotus1
        flag = True
        break
    if not daffodil:
        word = daffodil1
        flag = True
        break

if flag:
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")


if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants_stack:
    print(f"Consonants left: {' '.join(consonants_stack)}")
