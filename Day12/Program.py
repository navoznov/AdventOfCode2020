def get_clockwize_turn_count(turn_directon, angle):
    if turn_directon == 'L':
        turn_directon = 'R'
        angle = 360 - angle

    return int(angle / 90)


def get_direction_after_turn(current_direction, turn_directon, angle):
    turns_count = get_clockwize_turn_count(turn_directon, angle)

    turns = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E', }
    direction = current_direction
    for i in range(turns_count):
        direction = turns[direction]

    return direction


lines = open('Day12\input.txt').read().split('\n')
actions = [(l[0], int(l[1:])) for l in lines]
sum_koefs = {'N': ('Y', 1), 'E': ('X', 1), 'S': ('Y', -1), 'W': ('X', -1), }

# part 1
facing = 'E'
sums = {'X': 0, 'Y': 0}
for action in actions:
    directon, argument = action
    koef_info = sum_koefs.get(directon, None)
    if koef_info != None:
        axis, koef = koef_info
        sums[axis] += koef * argument
    elif directon == 'F':
        axis, koef = sum_koefs[facing]
        sums[axis] += koef * argument
    else:
        facing = get_direction_after_turn(facing, directon, argument)

print(abs(sums['X']) + abs(sums['Y']))

# part 2
koefs = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), }
waypoint = (10, 1)
ship = (0 , 0)

def sum_vectors(a, b):
    return tuple(map(lambda x, y: x + y, a, b))

def rotate_waypoint(waypoint):
    return (waypoint[1], -1 * waypoint[0])

for action in actions:
    directon, argument = action

    if directon == 'F':
        movement_vector = tuple([coord * argument for coord in waypoint])
        ship = sum_vectors(ship, movement_vector)
    elif directon == 'R' or directon == 'L':
        turn_count = get_clockwize_turn_count(directon, argument)
        for _ in range(turn_count):
            waypoint = rotate_waypoint(waypoint)
    else:
        vector = tuple([coordKoef * argument for coordKoef in koefs[directon]])
        waypoint = sum_vectors(waypoint, vector)

print(sum([abs(koord) for koord in ship]))
