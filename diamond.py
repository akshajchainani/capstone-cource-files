height = 5

for i in range(3, height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

for i in range(height - 2, -1, -1):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

