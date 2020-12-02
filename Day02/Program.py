import re

def parseLine(line):
    pattern = r'(\d+)-(\d+) (\w): (\w+)'
    match = re.match(pattern, line)
    return match.groups(0)

def isValidPasswordObj(obj):
    return isValidPassword(*obj)

def isValidPassword(minCount, maxCount, letter, password):
    minCount = int(minCount)
    maxCount = int(maxCount)
    counter = 0
    for ch in password:
        if ch == letter:
            counter += 1
            if counter > maxCount:
                return False

    return True if counter >= minCount else False

minCount, maxCount, letter, password = parseLine("16-20 h: hhhjthhhtphchpkhmhhh")
assert(isValidPasswordObj(parseLine("2-4 p: vpkpp")) == True)
assert(isValidPasswordObj(parseLine("2-4 v: vpkpp")) == False)

lines = open('Day02\input.txt').read().split('\n')

validPasswordsCounter = 0
for line in lines:
    minCount, maxCount, letter, password = parseLine(line)
    if isValidPassword(minCount, maxCount, letter, password):
        validPasswordsCounter += 1

print(validPasswordsCounter)
