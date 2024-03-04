def find_symbol(mm, sym):
    for row_index in range(n):
        for columns_index in range(n):
            if symbol == mm[row_index][columns_index]:
                return row_index, columns_index

n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)

if result:
    r_index, c_index = result
    print(f"({r_index}, {c_index})")

else:
    print(f"{symbol} does not occur in the matrix")
