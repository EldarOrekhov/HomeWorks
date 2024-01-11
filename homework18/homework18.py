# Task 1
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if 0 <= age <= 130:
        print(f"Привет, {name}! Твой возраст – {age}")
    else:
        raise ValueError
except:
    print("Error: age is number")

# Task 2.1
def greetingAndAge(name, age):
    if 0 <= age <= 130:
        return f"Привет, {name}! Твой возраст – {age}"
    else:
        raise ValueError

try:
    print(greetingAndAge(input("Enter your name: "), int(input("Enter your age: "))))
except:
    print("Error: age is number")

# Task 2.2
def greetingAndAge2(name, age):
    try:
        if 0 <= age <= 130:
            return f"Привет, {name}! Твой возраст – {age}"
        else:
            raise ValueError
    except:
        return "Error: age is number"
print(greetingAndAge2(input("Enter your name: "), input("Enter your age: ")))

# Task 3
try:
    lst = []
    num = 1
    while num != 0:
        num = int(input("Enter positive num or 0 to stop input: "))
        lst.append(num)
    sum = 0
    for i in lst:
        if i < 0:
            raise ValueError
        sum += i
    print(f"Sum of your numbers: {sum}")
except:
    print("Not correct input")

# Task 4.1
def calcSumOfNums(lst):
    sum = 0
    for i in lst:
        if i < 0:
            raise ValueError
        sum += i
    return f"Sum of your numbers: {sum}"
try:
    lst = []
    num = 1
    while num != 0:
        num = int(input("Enter positive num or 0 to stop input: "))
        lst.append(num)
    print(calcSumOfNums(lst))
except:
    print("Not correct input")

# Task 4.2
def calcSumOfNums2(lst):
    try:
        lst = [int(i) for i in lst]
        sum = 0
        for i in lst:
            if i < 0:
                raise ValueError
            sum += i
        return f"Sum of your numbers: {sum}"
    except:
        return "Not correct input"
lst = []
num = 1
while num != "0":
    num = input("Enter positive num or 0 to stop input: ")
    lst.append(num)
print(calcSumOfNums2(lst))
