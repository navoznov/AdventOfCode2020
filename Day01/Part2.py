def findTriple(numbers, sum):
    for i in range(len(numbers)-2):
        number1 = numbers[i]
        for j in range(i+1, len(numbers)-1):
            number2 = numbers[j]
            for k in range(j+1, len(numbers)):
                number3 = numbers[k]
                if sum == number1 + number2 + number3:
                    return (number1, number2, number3)


lines = open('Day01\input.txt').read().split('\n')
numbers = [int(line) for line in lines]
triple = findTriple(numbers, 2020)
print(triple[0] * triple[1] * triple[2])