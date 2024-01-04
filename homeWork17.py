# Task 1
def isAnagram(word1, word2):
    word1 = list(word1.replace(" ", ""))
    word2 = list(word2.replace(" ", ""))
    dict1 = {}
    dict2 = {}
    for i in word1:
        dict1[i] = dict1.get(i, 0) + 1
    for i in word2:
        dict2[i] = dict2.get(i, 0) + 1
    return dict1 == dict2

print(isAnagram("binary", "brainy"))

# Task 2
def taxiCalcPrice(km, minPrice=2, kmPrice=0.3):
    if km <= 3:
        return minPrice
    else:
        return minPrice + (km - 3) * kmPrice

print(f"Price for this trip will cost: {taxiCalcPrice(17.5)} y.o.")

# Task 3
from random import randint

def generatePass():
    password = []
    for i in range(randint(8, 15)):
        temp = randint(1, 3)
        if temp == 1:
            password.append(chr(randint(48, 57)))
        elif temp == 2:
            password.append(chr(randint(65, 90)))
        else:
            password.append(chr(randint(97, 122)))
    return ''.join(password)

print(generatePass())
print(generatePass())
print(generatePass())

# Task 4
def numsNOD(*args):
    nod = args[0]
    for i in args[1::]:
        while i:
            temp = nod
            nod = i
            i = temp % i
    return nod
print(numsNOD(*(165, 435, 300)))

# Task 5

numbers = [randint(-50, 50) for i in range(15)]
print(f"List: {numbers}")
print(list(filter(lambda x: x % 15 == 0, numbers)))

# Task 6
def changeDateFormat(date):
    date = date.split("/")
    errorMsg = "Помилка: неправильна дата"
    if len(date[0]) != 2 or len(date[1]) != 2 or len(date[2]) != 4:
        return errorMsg
    else:
        if int(date[1]) > 12 or int(date[1]) < 1:
            return errorMsg
        else:
            if int(date[1]) == 2:
                if not int(date[2]) % 4:
                    if int(date[0]) > 29 or int(date[0]) < 1:
                        return errorMsg
                else:
                    if int(date[0]) > 28 or int(date[0]) < 1:
                        return errorMsg
            elif int(date[1]) == 1 or int(date[1]) == 3 or int(date[1]) == 5 or int(date[1]) == 7 or int(date[1]) == 8 or int(date[1]) == 9 or int(date[1]) == 12:
                if int(date[0]) > 31 or int(date[0]) < 1:
                    return errorMsg
            else:
                if int(date[0]) > 30 or int(date[0]) < 1:
                    return errorMsg
    return f"{date[2]}-{date[1]}-{date[0]}"
print(changeDateFormat("01/01/2024"))
