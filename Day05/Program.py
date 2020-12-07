import re
lines = open('Day05\input.txt').read().split('\n')


def parseLine(line):
    replacements = {'F': '0', 'B': '1', 'R': '1', 'L': '0'}
    row = int(''.join([replacements[x] for x in line[:7]]), 2)
    column = int(''.join([replacements[x] for x in line[-3:]]), 2)
    return (row, column)


def getSeatId(row, column):
    return row * 8 + column


seatIds = [getSeatId(*(parseLine(x))) for x in lines]

# part 1
print(max(seatIds))

# part 2
seatIds.sort()
for i in range(len(seatIds)):
    if i+seatIds[0] != seatIds[i]:
        print(i+seatIds[0])
        break
