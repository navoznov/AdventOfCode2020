import re
lines = open('Day07\input.txt').read().split('\n')

# part 1
bags = []
for line in lines:
    mainColor, mapTo = line.split(' bags contain ')

    if mapTo.endswith('no other bags.'):
        continue
    toBags = [x.replace('bags', '').replace('bag', '').strip().split(' ', 1) for x in mapTo[:-1].split(', ')]
    bags = bags + [(color, mainColor) for _, color in toBags]

colors = set(['shiny gold'])
result = set()
while len(colors) > 0:
    bagsInfo = [(small, big) for small, big in bags if small in colors]
    colors = set([big for _, big in bagsInfo])
    result.update(colors)

print(len(result))

# part 2


def parseBags(line):
    mainColor, mapTo = line.split(' bags contain ')

    if mapTo.endswith('no other bags.'):
        return (mainColor, [])
    toBags = [x.replace('bags', '').replace('bag', '').strip().split(' ', 1) for x in mapTo[:-1].split(', ')]
    return (mainColor, toBags)


def getBagsCount(color):
    counter = 0
    bags = allBags[color]
    for count, color in bags:
        count = int(count)
        counter += count
        counter += count * getBagsCount(color)
    return counter


allBags = dict([parseBags(x) for x in lines])
print(getBagsCount('shiny gold'))
