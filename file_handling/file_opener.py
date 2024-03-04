try:
    file = open('text.txt', "r")
    print(f"File found")

except FileNotFoundError:
    print('File not found')
