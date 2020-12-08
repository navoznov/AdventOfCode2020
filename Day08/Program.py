import re

def parseInstraction(line):
    operation, argument = line.split(' ')
    argument = int(argument)
    return (operation, argument)

input = open('Day08\input.txt').read()
lines = input.split('\n')
instractions = [parseInstraction(line) for line in lines]

accumulator = 0
index = 0
history = []
while not index in history:
    operation, argument = instractions[index]
    history.append(index)
    if operation == 'jmp':
        index += argument
        continue

    if  operation == 'acc':
        accumulator +=argument
    index += 1

print(accumulator)
