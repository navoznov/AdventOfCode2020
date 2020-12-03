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

        x = (x + right) % width
        y += down
    return treesCounter


# part 1
print(getTreesCount(lines, 3, 1))

# part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for slope in slopes:
    result *= getTreesCount(lines, *slope)

print(result)