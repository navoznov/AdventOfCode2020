def findPair(numbers, sum):
    for i in range(len(numbers)-1):
        number1 = numbers[i]
        for j in range(i+1, len(numbers)):
            number2 = numbers[j]
            if sum == number1 + number2:
                return (number1, number2)

lines = open('Day01\input.txt').read().split('\n')
numbers = [int(line) for line in lines]
pair = findPair(numbers, 2020)
print(pair[0] * pair[1])