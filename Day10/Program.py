import datetime

numbers = [int(line) for line in open('Day10\input.txt').read().split('\n')]
min_diff = 1
max_diff = 3
start = 0
numbers.append(start)
numbers = sorted(numbers)
finish = numbers[-1] + max_diff
numbers.append(finish)

# part 1
counter = {1: 0, 2: 0, 3: 0}
diffs = [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]
for d in diffs:
    counter[d] += 1

print(counter[min_diff]*counter[max_diff])

# part 2
directions = {}
for i in range(len(numbers)-1):
    number = numbers[i]
    directions[number] = [
        n for n in numbers if min_diff <= n - number <= max_diff]

counts = {finish: 1}
for i in range(1, len(numbers)):
    number = numbers[i]
    counts[number] = sum([counts[d] for d in directions[number]])

print(counts[start])
