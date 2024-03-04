rows, columns = [int(x) for x in input().split()]

matrix = []

alphabet = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j",
            10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t",
            20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z",
            }

for n in range(rows):
    for i in range(columns):
        matrix.append(alphabet[n] + alphabet[i + n] + alphabet[n])
    print(" ".join(matrix))
    matrix.clear()

# r, c = [int(x) for x in input().split()]
#
# matrix = []
# start_index = ord("a")
#
# for row in range(start_index, start_index + r):
#     for col in range(start_index, start_index + c):
#         print(f"{chr(row)}{chr(row+col-start_index)}{chr(row)}", end=" ")
#     print()
#
