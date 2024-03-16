rows=5
for i in range(rows):
    for j in range((rows * 2)- 1):
        if i == rows - 1 or i + j == rows - 1 or j - i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()