# Task 1
num = int(input("Enter number: "))
i = 1
while i < 10:
    print(num, "*", i, "=", i * num)
    i += 1

# Task 2
userChoice = 1
while userChoice != 0:
    userChoice = int(input("Enter \"1\" if you want to convert USD($) to EUR(€)\n"
                           "Enter \"2\" if you want to convert EUR(€) to USD($)\n"
                           "Enter \"3\" if you want to convert USD($) to UAH(₴)\n"
                           "Enter \"4\" if you want to convert UAH(₴) to USD($)\n"
                           "Enter \"5\" if you want to convert EUR(€) to UAH(₴)\n"
                           "Enter \"6\" if you want to convert UAH(₴) to EUR(€)\n"
                           "Enter \"0\" to finish\n"))
    if userChoice == 0:
        continue
    elif userChoice == 1:
        money = float(input("Enter how many money you want to convert: "))
        print(str(money) + "$ =>", str(money * 0.95) + "€\n")
    elif userChoice == 2:
        money = float(input("Enter how many money you want to convert: "))
        print(str(money) + "€ =>", str(money * 1.06) + "$\n")
    elif userChoice == 3:
        money = float(input("Enter how many money you want to convert: "))
        print(str(money) + "$ =>", str(money * 36.47) + "₴\n")
    elif userChoice == 4:
        money = float(input("Enter how many money you want to convert: "))
        print(str(money) + "₴ =>", str(money * 0.027) + "$\n")
    elif userChoice == 5:
        money = float(input("Enter how many money you want to convert: "))
        print(str(money) + "€ =>", str(money * 38.55) + "₴\n")
    elif userChoice == 6:
        money = float(input("Enter how many money you want to convert: "))
        print(str(money) + "₴ =>", str(money * 0.026) + "€\n")
    else:
        print("Enter \"1\" or \"2\" or \"3\" or \"4\" or \"5\" or \"6\"\n")

# Task 3
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
number = int(input("Enter number: "))
while number < start or number > end:
    print("Number is not in range")
    number = int(input("Enter again: "))
i = start
while i <= end:
    if i == number:
        print("!" + str(i) + "!", end=' ')
    else:
        print(i, end=' ')
    i += 1