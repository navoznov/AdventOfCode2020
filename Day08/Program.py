import re


def parseInstraction(line):
    operation, argument = line.split(' ')
    argument = int(argument)
    return (operation, argument)


lines = open('Day08\input.txt').read().split('\n')
instractions = [parseInstraction(line) for line in lines]


def checkProgramTerminates(instractions):
    accumulator = 0
    index = 0
    history = []
    while True:
        if index == len(instractions):
            return True, accumulator

        if index in history:
            return False, accumulator

        operation, argument = instractions[index]
        history.append(index)
        if operation == 'jmp':
            index += argument
            continue

        if operation == 'acc':
            accumulator += argument
        index += 1


# part 1
_, accumulator = checkProgramTerminates(instractions)
print(accumulator)


# part 2

def getCorrectProgramAccumulator(instractions):
    replacements = [('nop', 'jmp'), ('jmp', 'nop')]

    for fromOperation, toOperation in replacements:
        for i in range(len(instractions)):
            operation, argument = instractions[i]
            if operation != fromOperation:
                continue
            instractions[i] = (toOperation, argument)
            result, accumulator = checkProgramTerminates(instractions)
            if result == True:
                return accumulator
            instractions[i] = (fromOperation, argument)


print(getCorrectProgramAccumulator(instractions))
