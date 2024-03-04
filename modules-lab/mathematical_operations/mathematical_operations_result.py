from mathematical_operations import *


try:
    data = mathematical_operations(*(input("Please enter first number, operator, second number: ").split()))
    print(f"{data:.2f}")

except (ValueError, KeyError):
    print("Enter a valid data!")
