# Task 2
num1 = int(input("Enter start of range: "))
num2 = int(input("Enter end of range: "))
if num1 < num2:
    i = num1
    i2 = num2
    i3 = num1
    i4 = num1
    count = 0
    print("1)", end=" ")
    while i <= num2:
        print(i, end=" ")
        i += 1
    print("\n2)", end=" ")
    while i2 >= num1:
        print(i2, end=" ")
        i2 -= 1
    print("\n3)", end=" ")
    while i3 <= num2:
        if i3 % 7 == 0 and i3 != 0:
            print(i3, end=" ")
        i3 += 1
    print("\n4)", end=" ")
    while i4 <= num2:
        if i4 % 5 == 0 and i4 != 0:
            count += 1
        i4 += 1
    print(count)
else:
    print("First number can't be bigger than second")

# Task 3
num1 = int(input("Enter start of range: "))
num2 = int(input("Enter end of range: "))
i = num1
while i <= num2:
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1