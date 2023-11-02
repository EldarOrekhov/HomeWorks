# Task 1
size = int(input("Enter size: "))
for i in range(1, size + 1):
    print(" " * (size - i) + "*" * (i*2-1))

# Task 2
size = int(input("Enter size: "))
for i in range(1, size + 1):
    print(" " * (size - i) + "*" * (i*2-1))
for i in range(size - 1, 0, -1):
    print(" " * (size - i) + "*" * (i*2-1))

# Task 3
size = int(input("Enter size: "))
for i in range(1, size + 1):
    if i == 1 or i == size:
        print(" " * (size - i) + "*" * (i*2-1))
    else:
        print(" " * (size - i) + "*" + " " * (i*2-3) + "*")