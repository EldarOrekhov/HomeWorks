from random import randint
# Task 1
field = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(field[1], field[2], field[3])
print(field[4], field[5], field[6])
print(field[7], field[8], field[9])
print("----------------------------")

turn = "X"
win = "*"
for i in range(5):
    while True:
        choice = int(input("Choice cell: "))
        if choice in field and choice != 0:
            field[choice] = turn
            turn = "0"
            break
    print(field[1], field[2], field[3])
    print(field[4], field[5], field[6])
    print(field[7], field[8], field[9])
    print("----------------------------")

    if field[1] != 1:
        if field[1] == field[2] and field[1] == field[3]:
            win = field[1]
        elif field[1] == field[4] and field[1] == field[7]:
            win = field[1]
        elif field[1] == field[5] and field[1] == field[9]:
            win = field[1]
    if field[2] != 2:
        if field[2] == field[5] and field[2] == field[8]:
            win = field[2]
    if field[3] != 3:
        if field[3] == field[6] and field[3] == field[9]:
            win = field[3]
    if field[4] != 4:
        if field[4] == field[5] and field[4] == field[6]:
            win = field[4]
    if field[7] != 7:
        if field[7] == field[8] and field[7] == field[9]:
            win = field[7]
        elif field[7] == field[5] and field[7] == field[3]:
            win = field[7]
    if win != "*":
        print(f"Winner: {win}")
        break
    while True:
        step = False
        if field[1] == "0":
            if field[2] == "0" and field[3] == 3:
                choice = 3
                step = True
            elif field[4] == "0" and field[7] == 7:
                choice = 7
                step = True
            elif field[5] == "0" and field[9] == 9:
                choice = 9
                step = True
        if field[2] == "0":
            if field[5] == "0" and field[8] == 8:
                choice = 8
                step = True
        if field[3] == "0":
            if field[2] == "0" and field[1] == 1:
                choice = 1
                step = True
            elif field[5] == "0" and field[7] == 7:
                choice = 7
                step = True
            elif field[6] == "0" and field[9] == 9:
                choice = 9
                step = True
        if field[4] == "0":
            if field[5] == "0" and field[6] == 6:
                choice = 6
                step = True
        if field[5] == "0":
            if field[5] == "0" and field[4] == 4:
                choice = 4
                step = True
        if field[7] == "0":
            if field[4] == "0" and field[1] == 1:
                choice = 1
                step = True
            elif field[5] == "0" and field[3] == 3:
                choice = 3
                step = True
            elif field[8] == "0" and field[9] == 9:
                choice = 9
                step = True
        if field[8] == "0":
            if field[5] == "0" and field[2] == 2:
                choice = 2
                step = True
        if field[9] == "0":
            if field[8] == "0" and field[7] == 7:
                choice = 7
                step = True
            elif field[5] == "0" and field[1] == 1:
                choice = 1
                step = True
            elif field[6] == "0" and field[3] == 3:
                choice = 3
                step = True

        if field[1] == "X":
            if field[2] == "X" and field[3] == 3:
                choice = 3
                step = True
            elif field[4] == "X" and field[7] == 7:
                choice = 7
                step = True
            elif field[5] == "X" and field[9] == 9:
                choice = 9
                step = True
        if field[2] == "X":
            if field[5] == "X" and field[8] == 8:
                choice = 8
                step = True
        if field[3] == "X":
            if field[2] == "X" and field[1] == 1:
                choice = 1
                step = True
            elif field[5] == "X" and field[7] == 7:
                choice = 7
                step = True
            elif field[6] == "X" and field[9] == 9:
                choice = 9
                step = True
        if field[4] == "X":
            if field[5] == "X" and field[6] == 6:
                choice = 6
                step = True
        if field[5] == "X":
            if field[5] == "X" and field[4] == 4:
                choice = 4
                step = True
        if field[7] == "X":
            if field[4] == "X" and field[1] == 1:
                choice = 1
                step = True
            elif field[5] == "X" and field[3] == 3:
                choice = 3
                step = True
            elif field[8] == "X" and field[9] == 9:
                choice = 9
                step = True
        if field[8] == "X":
            if field[5] == "X" and field[2] == 2:
                choice = 2
                step = True
        if field[9] == "X":
            if field[8] == "X" and field[7] == 7:
                choice = 7
                step = True
            elif field[5] == "X" and field[1] == 1:
                choice = 1
                step = True
            elif field[6] == "X" and field[3] == 3:
                choice = 3
                step = True
        if not step:
            choice = randint(1, 9)
        if choice in field:
            field[choice] = turn
            turn = "X"
            break
    print(field[1], field[2], field[3])
    print(field[4], field[5], field[6])
    print(field[7], field[8], field[9])
    if field[1] != 1:
        if field[1] == field[2] and field[1] == field[3]:
            win = field[1]
            print(f"Winner: {win}")
            break
        elif field[1] == field[4] and field[1] == field[7]:
            win = field[1]
            print(f"Winner: {win}")
            break
        elif field[1] == field[5] and field[1] == field[9]:
            win = field[1]
            print(f"Winner: {win}")
            break
    if field[2] != 2:
        if field[2] == field[5] and field[2] == field[8]:
            win = field[2]
            print(f"Winner: {win}")
            break
    if field[3] != 3:
        if field[3] == field[6] and field[3] == field[9]:
            win = field[3]
            print(f"Winner: {win}")
            break
    if field[4] != 4:
        if field[4] == field[5] and field[4] == field[6]:
            win = field[4]
            print(f"Winner: {win}")
            break
    if field[7] != 7:
        if field[7] == field[8] and field[7] == field[9]:
            win = field[7]
            print(f"Winner: {win}")
            break
        elif field[7] == field[5] and field[7] == field[3]:
            win = field[7]
            print(f"Winner: {win}")
            break
# Task 2
myLst = [randint(-50, 50) for i in range(15)]
lstEven = [i for i in myLst if not i % 2]
lstNotEven = [i for i in myLst if i % 2]
lstNegative = [i for i in myLst if i < 0]
lstPositive = [i for i in myLst if i >= 0]
print(f"List: {myLst}")
print(f"List with only even numbers: {lstEven}")
print(f"List with only not even numbers: {lstNotEven}")
print(f"List with only negative numbers: {lstNegative}")
print(f"List with only positive numbers: {lstPositive}")
