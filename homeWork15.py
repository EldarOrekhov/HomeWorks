# Task 1
def printText():
    print("\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\"\nBill Gates")
printText()

# Task 2
def evenInRange(num1, num2):
    print([i for i in range(num1, num2) if not i % 2])
evenInRange(1, 10)

# Task 3
def drawSquare(sideSize, char, isFilled):
    if isFilled:
        for i in range(sideSize):
            print(char*sideSize)
    else:
        for i in range(sideSize):
            if i == 0 or i == sideSize-1:
                print(char * sideSize)
            else:
                print(char, (" " * (sideSize-4)), char)
drawSquare(5, "&", False)

# Task 4
def findMin(num1, num2, num3, num4, num5):
    minNum = num1
    if minNum > num2:
        minNum = num2
    if minNum > num3:
        minNum = num3
    if minNum > num4:
        minNum = num4
    if minNum > num5:
        minNum = num5
    return minNum
print(findMin(1, 2, 3, 4, 5,))

# Task 5
def multiplyInRange(num1, num2):
    if num1 < num2:
        count = 1
        for i in range(num1, num2+1):
            count *= i
    else:
        count = 1
        for i in range(num2, num1+1):
            count *= i
    return count
print(multiplyInRange(25, 5))

# Task 6
def countNumLen(num):
    return len(str(num))
print(countNumLen(3456))

# Task 7
def isPalindrom(num):
    return str(num) == str(num)[::-1]
print(isPalindrom(123321))