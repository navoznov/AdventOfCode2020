input = open('Day15\input.txt').read()


def get_prev_index(number, numbers):
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] == number:
            return i

    return -1

# part 1
def run1(input):
    numbers = [int(x) for x in input.split(',')]
    last = numbers[-1]
    for i in range(len(numbers), 2020):
        prev_index = get_prev_index(last, numbers)
        last = 0 if prev_index == -1 else (i - 1) - prev_index
        numbers.append(last)

    return last


print(run1(input))
