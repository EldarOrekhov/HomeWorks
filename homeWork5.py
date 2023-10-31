# Task1
price = float(input("Enter price per minute: "))
talkTime = float(input("Enter duration in minutes: "))
operIncoming = input("Choose incoming operator: 1.Kyivstar, 2.Vodafone, 3.Lifecell: ")
operOutgoing = input("Choose outgoing operator: 1.Kyivstar, 2.Vodafone, 3.Lifecell: ")
if operOutgoing == "1":
    if operIncoming == "1":
        print("Call cost =", price * talkTime)
    elif operIncoming == "2":
        print("Call cost =", price * talkTime * 1.2)
    elif operIncoming == "3":
        print("Call cost =", price * talkTime * 1.4)
elif operOutgoing == "2":
    if operIncoming == "2":
        print("Call cost =", price * talkTime)
    elif operIncoming == "1":
        print("Call cost =", price * talkTime * 1.2)
    elif operIncoming == "3":
        print("Call cost =", price * talkTime * 1.4)
elif operOutgoing == "3":
    if operIncoming == "3":
        print("Call cost =", price * talkTime)
    elif operIncoming == "1":
        print("Call cost =", price * talkTime * 1.2)
    elif operIncoming == "3":
        print("Call cost =", price * talkTime * 1.4)

# Task 2
sales = [0,0,0]
sales[0] = float(input("Enter first manager sales: "))
sales[1] = float(input("Enter second manager sales: "))
sales[2] = float(input("Enter third manager sales: "))
for i in range(3):
    if sales[i] < 500:
        sales[i] = 200 + sales[i] * 0.03
    elif sales[i] < 1000:
        sales[i] = 200 + sales[i] * 0.05
    else:
        sales[i] = 200 + sales[i] * 0.08
    print("Salary of", i + 1, "manager is", sales[i], "$")
if sales[0] > sales[1] and sales[0] > sales[2]:
    bestManager = 1
elif sales[1] > sales[0] and sales[1] > sales[2]:
    bestManager = 2
else:
    bestManager = 3
print("Best manager is", bestManager, "his salary with bonus =", sales[bestManager - 1] + 200)

# Task 3
firstX = int(input("Enter row number of first cell: "))
firstY = int(input("Enter column number of first cell: "))
secondX = int(input("Enter row number of second cell: "))
secondY = int(input("Enter column number of second cell: "))
if firstX == secondX or firstY == secondY:
    print("YES")
else:
    print("NO")

# Task 4
firstX = int(input("Enter row number of first cell: "))
firstY = int(input("Enter column number of first cell: "))
secondX = int(input("Enter row number of second cell: "))
secondY = int(input("Enter column number of second cell: "))
if firstX + firstY == secondX + secondY or firstX - firstY == secondX - secondY:
    print("YES")
else:
    print("NO")