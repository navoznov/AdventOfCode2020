groups = open('Day06\input.txt').read().split('\n\n')

# part 1
sum = 0
for group in groups:
    sum += len(set([x for x in group if x != '\n']))

print(sum)

# part 2
sum = 0
for group in groups:
    frequency = {}
    for letter in group:
        frequency[letter] = frequency.get(letter, 0) + 1

    peopleCount = frequency.get('\n', 0) + 1
    sum += len([letter for letter, count in frequency.items() if count == peopleCount])

print(sum)
