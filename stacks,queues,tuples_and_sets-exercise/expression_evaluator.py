from collections import deque

expressions = input().split()
nums = deque()

operators = { "*": lambda a, b: a * b,
             "+": lambda a, b: a + b,
             "-": lambda a, b: a - b,
             "/": lambda a, b: a // b,
}
for char in expressions:
    if char in "+-/*":
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operators[char](left, right)
            nums.appendleft(result)

    else:
        nums.append(int(char))

print(nums.popleft())
