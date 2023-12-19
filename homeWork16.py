from random import randint
import requests
# Task 1
myLst = [randint(-50, 50) for i in range(5)]
def reverseNums(lst):
    return lst[::-1]
print(f"List: {myLst}\nReversed list: {reverseNums(myLst)}")

# Task 2
myLst = [1, 2, 3, 4, 5]
def findNum(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return f"index of {num}: {i}"
    return "Number is not in list"
print(findNum(myLst, 5))

# Task 3
myLst = [1, 2, 3, 4, 5]
def factorialList(lst):
    newLst = []
    for i in lst:
        temp = 1
        for j in range(1, i+1):
            temp *= j
        newLst.append(temp)
    return newLst
print(factorialList(myLst))

# Task 4
myLst = [1, 2, 3, 4, 5]
def multList(lst):
    temp = 1
    for i in lst:
        temp *= i
    return temp
print(multList(myLst))

# Task 5
myLst = [randint(-50, 50) for i in range(10)]
def findMin(lst):
    minNum = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < minNum:
            minNum = lst[i]
    return minNum
print(f"List: {myLst}\nMinimal number in list: {findMin(myLst)}")

# Task 6
myLst = [randint(0, 50) for i in range(5)]
def countPrimes(lst):
    count = 0
    for num in lst:
        if num < 2:
            continue
        for i in range(2, int(num // 2) + 1):
            if num % i == 0:
                count -= 1
                break
        count += 1
    return count
print(f"List: {myLst}\nPrimes in list: {countPrimes(myLst)}")
# Task 7
url = "https://api.openweathermap.org/data/2.5/weather/"
TOKEN = "8cd37a85cb531687fb540b8030c7248e"
params = {
    "q": input("City: ").title(),
    "appid": TOKEN,
    "units": "metric"
}
data = requests.get(url, params=params)
data = data.json()
print(f'Temperature in {data["name"]} {data["sys"]["country"]} {data["main"]["temp"]}°\nWind speed {data["wind"]["speed"]} M/S')
