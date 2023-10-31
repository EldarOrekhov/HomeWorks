# Task 1
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for i in range(start, end + 1):
    num = True
    for j in range(2, i):
        if i % j == 0:
            num = False
            break
    if num:
        print(i)

# Task 2
lineBreak = 0
for i in range(1, 11):
    for j in range(1, 11):
        print(str(i) + "*" + str(j), "=", i * j, end="   ")
        lineBreak += 1
        if lineBreak == 10:
            print()
            lineBreak = 0

# Task 3
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
lineBreak = 0
for i in range(start, end + 1):
    for j in range(1, 11):
        print(str(i) + "*" + str(j), "=", i * j, end="   ")
        lineBreak += 1
        if lineBreak == 10:
            print()
            lineBreak = 0