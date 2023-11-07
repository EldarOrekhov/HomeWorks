while True:
    userChoice = input("Enter what figure you want to draw\n"
                       "You can enter: \"а\",\"б\",\"в\",\"г\",\"д\",\"е\",\"ж\",\"з\",\"и\",\"к\"\n"
                       "Enter 0 to finish\n")
    match userChoice:
        case "0":
            break
        case "а":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size):
                    if i == j or i < j or i == 0:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "б":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size):
                    if i == j or j == 0 or i > j:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "в":
            size = int(input("Enter size: "))
            for i in range(size, 0, -1):
                for j in range(size * 2 - 1):
                    if j >= size - i and j < size + i - 1:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "г":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size * 2 - 1):
                    if j >= size - 1 - i and j <= size - 1 + i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "д":
            size = int(input("Enter size: "))
            for i in range(size, 0, -1):
                for j in range(size * 2 - 1):
                    if j >= size - i and j < size + i - 1:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
            for i in range(size):
                for j in range(size * 2 - 1):
                    if j >= size - 1 - i and j <= size - 1 + i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "е":
            size = int(input("Enter size: "))
            for i in range(size, 0, -1):
                for j in range(size * 2):
                    if j >= size - i and j < size + i:
                        print(" ", end='')
                    else:
                        print("*", end='')
                print()
            for i in range(size * 2):
                print("*", end='')
            print()
            for i in range(size):
                for j in range(size * 2):
                    if j >= size - 1 - i and j <= size + i:
                        print(" ", end='')
                    else:
                        print("*", end='')
                print()
        case "ж":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size):
                    if j <= i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
            for i in range(size - 1, 0, -1):
                for j in range(size):
                    if j < i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "з":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size):
                    if j >= size - 1 - i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
            for i in range(size - 1, 0, -1):
                for j in range(size):
                    if j >= size - i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "и":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size):
                    if i == 0 or j == 0 or j < size-i:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case "к":
            size = int(input("Enter size: "))
            for i in range(size):
                for j in range(size):
                    if i == size-1 or j == size - 1 or j >= size - i - 1:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
        case _:
            print("Incorrect input")