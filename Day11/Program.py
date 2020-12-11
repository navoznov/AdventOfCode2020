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

def get_seat_next_state(x, y, map, rules):
    get_adjecent_seats_func, min_occupied_adjacent_seat_count = rules

    current_seat_state = map[y][x]
    if current_seat_state == FLOOR:
        return FLOOR

    adjacent_seats = get_adjecent_seats_func(x, y, map)
    if current_seat_state == FLOOR:
        return FLOOR

    occupied_adjacent_seat_count = len([s for s in adjacent_seats if s == OCCUPIED])

    if current_seat_state == EMPTY and occupied_adjacent_seat_count != 0 or current_seat_state == OCCUPIED and occupied_adjacent_seat_count >= min_occupied_adjacent_seat_count:
        return EMPTY
    return OCCUPIED

def get_next_map(map, rules):
    next_map = []
    for y in range(len(map)):
        line = map[y]
        line2 = ''.join([get_seat_next_state(x, y, map, rules)
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


def get_stable_map_occupied_seat_count(map, rules):
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

        map = get_next_map(map, rules)
        prev_occupied_seat_count = occupied_seat_count
        step += 1
    return prev_occupied_seat_count

map = open('Day11\input.txt').read().split('\n')

# part 1
def get_adjecent_seats(x, y, map):
    sizeX = len(map[0])
    sizeY = len(map)

    directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

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
    return adjacent_seats

rules1 = (get_adjecent_seats, 4)
print(get_stable_map_occupied_seat_count(map, rules1))

# part 2

def get_first_visible_seat_by_direction(x, y, map, direction):
    dx, dy = direction
    sizeX = len(map[0])
    sizeY = len(map)
    while True:
        x, y = x + dx, y + dy
        if x < 0 or y < 0 or x > sizeX - 1 or y > sizeY - 1:
            return FLOOR
        if map[y][x] != FLOOR:
            return map[y][x]

def get_adjecent_seats(x, y, map):
    directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    adjacent_seats = [seat for seat in [get_first_visible_seat_by_direction(x, y, map, d) for d in directions] if seat != FLOOR]
    return adjacent_seats

rules2 = (get_adjecent_seats, 5)
print(get_stable_map_occupied_seat_count(map, rules2))
