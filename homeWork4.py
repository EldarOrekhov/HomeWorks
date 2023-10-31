# Task 5
password = "123"
userPass = input("Enter password: ")
if userPass == password:
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")

# Task 6
num = input("Enter four-digit number: ")
for digit in num:
    if digit == "0":
        print("Zero")
    elif digit == "1":
        print("One")
    elif digit == "2":
        print("Two")
    elif digit == "3":
        print("Three")
    elif digit == "4":
        print("Four")
    elif digit == "5":
        print("Five")
    elif digit == "6":
        print("Six")
    elif digit == "7":
        print("Seven")
    elif digit == "8":
        print("Eight")
    elif digit == "9":
        print("Nine")

# Task 7
temperature = float(input("Enter temperature: "))
if temperature <= 0:
    print("A cold, isn’t it?")
elif 0 < temperature < 10:
    print("Cool.")
else:
    print("Nice weather we’re having.")