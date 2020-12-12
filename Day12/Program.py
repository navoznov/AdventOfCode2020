def get_facing_after_turn(current_facing, directon, angle):
    if directon == 'L':
        directon = 'R'
        angle = 360 - angle

    turns = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E', }
    turns_count = int(angle / 90)
    facing = current_facing
    for i in range(turns_count):
        facing = turns[facing]

    return facing

lines = open('Day12\input.txt').read().split('\n')
actions = [(l[0], int(l[1:])) for l in lines]
facing = 'E'
sums = {'N': 0, 'E': 0, 'S': 0, 'W': 0, }
for action in actions:
    directon, argument = action
    if directon in sums.keys():
        sums[directon] += argument
    elif directon == 'F':
        sums[facing] += argument
    else:
        facing = get_facing_after_turn(facing, directon, argument)

print(abs(sums['N'] - sums['S']) + abs(sums['E'] - sums['W']))