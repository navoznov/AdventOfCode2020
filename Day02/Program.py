import re

def parseLine(line):
    pattern = r'(\d+)-(\d+) (\w): (\w+)'
    match = re.match(pattern, line)
    return match.groups(0)

def isValidPasswordPart1(minCount, maxCount, letter, password):
    minCount = int(minCount)
    maxCount = int(maxCount)
    counter = 0
    for ch in password:
        if ch == letter:
            counter += 1
            if counter > maxCount:
                return False

    return True if counter >= minCount else False

def isValidPasswordPart2(position1, position2, letter, password):
    letter1 = password[int(position1)-1]
    letter2 = password[int(position2)-1]
    return letter1 == letter and letter2 != letter or letter1 != letter and letter2 == letter

lines = open('Day02\input.txt').read().split('\n')

# part 1
validPasswordsCounter = 0
for line in lines:
    minCount, maxCount, letter, password = parseLine(line)
    if isValidPasswordPart1(minCount, maxCount, letter, password):
        validPasswordsCounter += 1

print(validPasswordsCounter)

# part 2
validPasswordsCounter = 0
for line in lines:
    position1, position2, letter, password = parseLine(line)
    if isValidPasswordPart2(position1, position2, letter, password):
        validPasswordsCounter += 1

print(validPasswordsCounter)