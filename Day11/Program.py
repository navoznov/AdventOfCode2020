import datetime

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def add_floor_border(map):
    map = ['.' + line + '.' for line in map]
    floor_line = ''.join(['.' for _ in range(len(map[0]))])
    map.insert(0, floor_line)
    map.append(floor_line)
    return map


def get_seat_next_state(x, y, map):
    current_seat_state = map[y][x]
    if current_seat_state == FLOOR:
        return FLOOR

    sizeX = len(map[0])
    sizeY = len(map)
    adjacent_seats = []

    if x > 0:
        adjacent_seats.append(map[y][x-1])
        if y > 0:
            adjacent_seats.append(map[y-1][x-1])
        if y < sizeY - 1:
            adjacent_seats.append(map[y+1][x-1])

    if x < sizeX - 1:
        adjacent_seats.append(map[y][x+1])
        if y > 0:
            adjacent_seats.append(map[y-1][x+1])
        if y < sizeY - 1:
            adjacent_seats.append(map[y+1][x+1])

    if y > 0:
        adjacent_seats.append(map[y-1][x])
    if y < sizeY - 1:
        adjacent_seats.append(map[y+1][x])

    return get_seat_next_state_by_adjacents(current_seat_state, adjacent_seats)


def get_seat_next_state_by_adjacents(current_seat_state, adjacent_seats):
    if current_seat_state == FLOOR:
        return FLOOR

    occupied_adjacent_seat_count = len([s for s in adjacent_seats if s == OCCUPIED])

    if current_seat_state == EMPTY and occupied_adjacent_seat_count != 0 or current_seat_state == OCCUPIED and occupied_adjacent_seat_count >= 4:
        return EMPTY
    return OCCUPIED

def get_next_map(map):
    next_map = []
    for y in range(len(map)):
        line = map[y]
        line2 = ''.join([get_seat_next_state(x, y, map)
                         for x in range(len(line))])
        next_map.append(line2)
    return next_map


def print_map(map):
    for line in map:
        print(line)


def get_seat_count(map, seat_type):
    counter = 0
    for line in map:
        counter += len([x for x in line if x == seat_type])
    return counter


map = open('Day11\input.txt').read().split('\n')

step = 0
prev_occupied_seat_count = -1
while True:
    occupied_seat_count = get_seat_count(map, OCCUPIED)

    # print('Step = ', step)
    # print('Occupied seat count = ', occupied_seat_count)
    # print_map(map)
    # print()

    if occupied_seat_count == prev_occupied_seat_count:
        break

    map = get_next_map(map)
    prev_occupied_seat_count = occupied_seat_count
    step += 1

print(prev_occupied_seat_count)
