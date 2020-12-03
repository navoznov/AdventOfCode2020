import re
lines = open('Day03\input.txt').read().split('\n')

def getTreesCount(lines, right, down):
    treesCounter = 0
    y = 0
    x = 0
    width = len(lines[0])
    while y < len(lines):
        line = lines[y]
        if line[x] == '#':
            treesCounter += 1

        x = (x + 3) % width
        y  += down
    return treesCounter

print(getTreesCount(lines, 3, 1))