input = open('Day15\input.txt').read()


def get_nth_number(n, start_numbers):
    numbers = start_numbers
    last = numbers[-1]
    indexes = dict([(numbers[i], i) for i in range(len(numbers)-1)])
    for i in range(len(numbers), n):
        prev_index = indexes.get(last, -1)
        indexes[last] = i - 1
        last = 0 if prev_index == -1 else (i - 1) - prev_index

    return last

numbers = [int(x) for x in input.split(',')]

# part 1
print(get_nth_number(2020, numbers))

# part 2
print(get_nth_number(30000000, numbers))