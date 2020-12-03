import re
lines = open('Day03\input0.txt').read().split('\n')

treesCounter = 0
x = 0
width = len(lines[0])
for line in lines:
    if line[x] == '#':
        treesCounter += 1

    x = (x + 3) % width

print(treesCounter)