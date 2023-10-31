# Task 1
diameter = float(input("Enter the diameter of the circle: "))
userChoice = int(input("Enter \"1\" if you want to calculate area of the circle\n"
    "Enter \"2\" if you want to calculate perimetr of the circle\n"))
if userChoice == 1:
    print("Area of your circle:", 3.14 * (diameter / 2) ** 2)
elif userChoice == 2:
    print("Perimetr of your circle:", 3.14 * diameter)
else:
    print("Enter \"1\" or \"2\"")

# Task 2
price = float(input("Enter price of one game console: "))
quantity = int(input("Enter quantity of consoles: "))
discount = float(input("Enter discount percent: "))
userChoice = int(input("Enter \"1\" if you want to calculate total order amount\n"
    "Enter \"2\" if you want to calculate price of one console with discount\n"))
if userChoice == 1:
    print("Total order amount:", price * quantity * (1 - discount / 100))
elif userChoice == 2:
    print("Price of one console with discount:", price * (1 - discount / 100))
else:
    print("Enter \"1\" or \"2\"")

# Task 3
fileSize = float(input("Enter file size in gigabytes: "))
internetSpeed = float(input("Enter internet connection speed in bits per second: "))
userChoice = int(input("Enter \"1\" if you want to calculate file download time in minutes\n"
    "Enter \"2\" if you want to calculate file download time in seconds\n"))
if userChoice == 1:
    print("File will download for:", fileSize * 8 * 10**9 / internetSpeed / 60, "minutes")
elif userChoice == 2:
    print("File will download for:", fileSize * 8 * 10**9 / internetSpeed, "seconds")
else:
    print("Enter \"1\" or \"2\"")