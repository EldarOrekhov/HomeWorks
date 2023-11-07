# Task 1
line = input("Enter line: ")
symbol = input("Enter symbol to count: ")
count = 0
if len(symbol) > 1:
    print("Enter 1 symbol only")
else:
    for i in line:
        if i == symbol:
            count += 1
    print(f"Symbol \"{symbol}\" appears in the text {count} times")

# Task 2
line = input("Enter line: ").lower()
word = input("Enter word to count: ")
print(f"Word \"{word}\" appears in the text {line.count(word.lower())} times")

# Task 3
line = input("Enter line: ")
firstWord = input("Enter word you want to change: ")
secondWord = input("Enter word to be replaced with: ")
print(line.replace(firstWord, secondWord))