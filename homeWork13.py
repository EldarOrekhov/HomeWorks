# Task 1
import random
lst = []
for i in range(10):
    lst.append(random.randint(-100, 100))
print(lst)
minNum = lst[0]
maxNum = lst[0]
for temp in lst:
    if temp < minNum:
        minNum = temp
    if temp > maxNum:
        maxNum = temp

negative = 0
positive = 0
zeros = 0
for elem in lst:
    if elem < 0:
        negative += 1
    elif elem > 0:
        positive += 1
    else:
        zeros += 1

print(f"Minimal element: {minNum}")
print(f"Max element: {maxNum}")
print(f"Negative elements: {negative}")
print(f"Positive elements: {positive}")
print(f"Number of zeros: {zeros}")

# Task 2

heights = input("Enter heights list separated by space: ").split()
petyaHeight = int(input("Enter Petyas height: "))
position = 1
for i in range(len(heights)):
    if petyaHeight > int(heights[i]):
        break
    position += 1

print(f"Petyas position: {position}")
