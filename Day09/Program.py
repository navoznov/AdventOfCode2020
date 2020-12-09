all_numbers = [int(x) for x in open('Day09\input.txt').read().split('\n')]

# part 1
def check_sum(number, numbers):
    for n1 in numbers:
        for n2 in numbers:
            if n1 != n2 and n1+n2 == number:
                return True

    return False

def get_first_invalid_number():
    for i in range(25, len(all_numbers)):
        numbers = all_numbers[i-25:i+1]
        number = all_numbers[i]
        if not check_sum(number, numbers):
            return number

first_invalid_number = get_first_invalid_number()
print(first_invalid_number)

# part 2
def get_sequence(first_invalid_number, all_numbers):
    for i in range(len(all_numbers)-1):
        if all_numbers[i] >=first_invalid_number:
            continue

        for j in range(len(all_numbers)-1):
            numbers = all_numbers[i:i+j+1]
            total = sum(numbers)
            if total > first_invalid_number:
                break

            if total == first_invalid_number:
                return numbers

sequence = get_sequence(first_invalid_number, all_numbers)
print(min(sequence) + max(sequence))
