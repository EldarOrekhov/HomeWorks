# Task 1
def compareFiles(file1Path, file2Path):
    with open(file1Path, 'r', encoding='utf-8') as file1, open(file2Path, 'r', encoding='utf-8') as file2:
        lines_file1 = file1.readlines()
        lines_file2 = file2.readlines()

        min_len = min(len(lines_file1), len(lines_file2))

        filesIdentical = True

        for i in range(min_len):
            if lines_file1[i] != lines_file2[i]:
                print(f"File1: {lines_file1[i].strip()}")
                print(f"File2: {lines_file2[i].strip()}")
                print("---------------------")
                filesIdentical = False

        if len(lines_file1) > len(lines_file2):
            filesIdentical = False
            for i in range(min_len, len(lines_file1)):
                print(f"File1: {lines_file1[i].strip()}")
        elif len(lines_file1) < len(lines_file2):
            filesIdentical = False
            for i in range(min_len, len(lines_file2)):
                print(f"File2: {lines_file2[i].strip()}")
        if filesIdentical:
            print("Files identical")

compareFiles('file1.txt', 'file2.txt')

# Task 2

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    vowels = 'aeiouаеёиоуыэюя'

    num_characters = len(content)
    num_lines = content.count('\n')
    num_vowels = len([1 for char in content if char.lower() in vowels])
    num_consonants = len([1 for char in content if char.lower() not in vowels])
    num_digits = len([1 for char in content if char.isdigit()])

    output_file_path = 'statistics.txt'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f"Количество символов: {num_characters}\n")
        output_file.write(f"Количество строк: {num_lines}\n")
        output_file.write(f"Количество гласных букв: {num_vowels}\n")
        output_file.write(f"Количество согласных букв: {num_consonants}\n")
        output_file.write(f"Количество цифр: {num_digits}\n")

    print(f"Succes write to: {output_file_path}")

analyze_text('file1.txt')

# Task 3

def remove_last_line(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if lines:
        lines = lines[:-1]

    output_file_path = 'fileWithoutLine.txt'

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines)

    print(f"Последняя строка успешно удалена из файла {input_file_path}. Результат записан в файл {output_file_path}")

remove_last_line('file1.txt')

# Task 4

def findLongestLine(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    longest_line_length = max(len(line) for line in lines)

    print(f"Longest line have: {longest_line_length} symbols")

findLongestLine('file1.txt')

# Task 5

def countWord(file_path, target_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.lower().count(target_word.lower())

    print(f"Word '{target_word}' is {words} in file")

target_word = input("Enter word to find in file: ")

countWord('file1.txt', target_word)

# Task 6

def find_and_replace(file_path, target_word, replacement):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content_modified = content.replace(target_word, replacement)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content_modified)

    print(f"Word '{target_word}' changed to '{replacement}' in file: {file_path}")

target_word = input("Enter word to find: ")
replacement = input("Enter word to change: ")

find_and_replace('file1.txt', target_word, replacement)
