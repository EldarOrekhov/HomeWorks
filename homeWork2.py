# Task 1
name = input("Enter your name: ")
age = input("Enter your age: ")
phoneNumber = input("Enter your phone number: ")
print("Hello,", name, "your age:", age, "years", "Phone number:", phoneNumber)

# Task 2 if n + n*n + n*n*n
n = int(input("Enter number: "))
print(n + n*n + n*n*n)

# Task 2 if n + nn + nnn
n = int(input("Enter number: "))
doubleN = str(n) + str(n)
tripleN = str(n) + str(n) + str(n)
print(n + int(doubleN) + int(tripleN))

# Task 3
num = int(input("Enter number: "))
print("Previous:", num - 1)
print("Next:", num + 1)

# Task 4
number = float(input("Enter any three-digit positive number: "))
print("First digit:", (number - number % 100) / 100)
print("Second digit:", (number % 100 - number % 10) / 10)
print("Third digit:", number % 10)