# Task 1
text = ("1. змінити текст таким чином, щоб кожне речення починалося з великої літери; "
        "2. порахуйте скільки разів цифри зустрічаються в тексті! "
        "3. порахуйте скільки разів розділові знаки зустрічаються в тексті; "
        "4. порахуйте кількість знаків оклику в тексті!")
digits = 0
punctuation = 0
excl = 0
for i in text:
    if i == "," or i == ";" or i == ":":
        punctuation += 1
    elif i.isdigit():
        digits += 1
    elif i == "!":
        excl += 1
temp = text.split()
for i in range(len(temp)-1):
    if temp[i].endswith(".") or temp[i].endswith("!") or temp[i].endswith("?"):
        temp[i+1] = temp[i+1].capitalize()
for i in temp:
    print(i, end=" ")
print()
print(f"Digits: {digits}")
print(f"Punctuation: {punctuation}")
print(f"Exclamation points: {excl}")

# Task 2
userInput = input("Enter numbers list separated by space: ")
numberCount = input("Enter what number you want to count: ")
count = 0
if userInput.replace(" ", "").isdigit() and numberCount.isdigit():
    numbersList = userInput.split()
    for i in numbersList:
        if i == numberCount:
            count += 1
    print(f"Number {numberCount} found {count} times")
else:
    print("Enter only numbers")

# Task 3
userInput = input("Enter numbers list separated by space: ")
average = 0
sumOfNums = 0
if userInput.replace(" ", "").isdigit():
    numbersList = userInput.split()
    for i in numbersList:
        sumOfNums += int(i)
    average = sumOfNums / len(numbersList)
    print(f"Average: {average}\nSum: {sumOfNums}")
else:
    print("Enter only numbers")

# Task 4
userInput = input("Enter your math problem: ").replace(" ", "")
action = 0
for i in range(len(userInput)):
    if userInput[i].isdigit():
        continue
    else:
        action = userInput[i]
if action == 0:
    print("Incorrect input")
else:
    firstNum = int(userInput.split(action)[0])
    secondNum = int(userInput.split(action)[1])
    if action == "+":
        print(firstNum + secondNum)
    elif action == "-":
        print(firstNum - secondNum)
    elif action == "*":
        print(firstNum * secondNum)
    elif action == "/":
        print(firstNum / secondNum)
    else:
        print("Incorrect input")