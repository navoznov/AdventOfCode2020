import math

def parse_range(str):
    return tuple([int(x) for x in str.split('-')])


def parse_input(input):
    lines = input.split('\n')
    counter = 0

    field_rules = {}
    for i in range(len(lines)):
        line = lines[i]
        if line == '':
            break
        name, rangesStr = line.split(':')
        field_rules[name] = [parse_range(r) for r in rangesStr.split(' or ')]

    my_ticket = [int(x) for x in lines[i + 2].split(',')]

    other_tickets = [[int(x) for x in lines[j].split(',')]
                     for j in range(i + 5, len(lines))]
    return (field_rules, my_ticket, other_tickets)


def is_in_range(value, range):
    min, max = range
    return min <= value <= max


def is_error(value, ranges):
    for r in ranges:
        if is_in_range(value, r):
            return False

    return True


input = open('Day16\input.txt').read()
field_rules, my_ticket, tickets = parse_input(input)

all_ranges = []
all_ranges = [r for rr in field_rules.values() for r in rr]

# part 1
errors = [x for t in tickets for x in t if is_error(x, all_ranges)]
print(sum(errors))


# part 2
def check_all_values_are_valid(values, rules):
    for value in values:
        if is_error(value, rules):
            return False

    return True

def get_indexes_for_field_rules(field_rules, pivot_ticket_values, excluded_indexes):
    _, rules = field_rules
    result = []
    indexes = [index for index in range(len(pivot_ticket_values)) if index not in excluded_indexes]
    for index in indexes:
        values = pivot_ticket_values[index]
        if check_all_values_are_valid(values, rules):
            result.append(index)
    return result


tickets = [t for t in tickets if check_all_values_are_valid(t, all_ranges)]
field_indexes = {}
START_WORD = 'departure'
DEPTURE_WORD_COUNT = 6
field_rules = list(field_rules.items())
pivot_ticket_values = [[t[i] for t in tickets] for i in range(len(field_rules))]
while len([f for f, i in field_indexes.items() if f.startswith(START_WORD)]) < DEPTURE_WORD_COUNT:
    for i in range(len(field_rules)):
        field, rules = field_rules[i]
        if field_indexes.get(field, None) != None:
            continue

        indexes = get_indexes_for_field_rules(field_rules[i], pivot_ticket_values, field_indexes.values())
        if len(indexes) == 1:
            field_indexes[field] = indexes[0]

print(math.prod([my_ticket[i] for f, i in field_indexes.items() if f.startswith(START_WORD)]))