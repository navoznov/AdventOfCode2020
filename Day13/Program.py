
timestampStr, busesStr = open('Day13\input.txt').read().split('\n')

# part 1
timestamp = int(timestampStr)
buses = [int(bus) for bus in busesStr.split(',') if bus != 'x']
buses_after_timestamp = [((int(timestamp / bus) + 1) * bus, bus) for bus in buses]
bus_timestamp, bus = min(buses_after_timestamp)
print(bus * (bus_timestamp - timestamp))

# part 2
buses = [bus for bus in busesStr.split(',')]

bus_times = []
for i in range(len(buses)):
    bus = buses[i]
    if bus == 'x':
        continue

    bus_times.append((int(bus), i))

bus_times.sort()
bus_times.reverse()

def check_timestamp(timestamp, bus_times):
    for bus, time in bus_times:
        if (timestamp + time) % bus != 0:
            return False

    return True


#[(787, 48), (523, 17), (41, 7), (37, 54), (29, 77), (23, 40), (19, 36), (17, 0), (13, 35)]

# 787 48
# 523 17
# 41  7
# 37  54
# 29  77
# 23  40
# 19  36
# 17  0
# 13  35

def get_timestamp():
    increment, time = bus_times[0]
    start = int("203,480,886,435,643".replace("," ,""))
    timestamp = (start  - (start % increment)) - time
    timestamp -= increment
    while True:
        timestamp += increment
        if (timestamp) % 17 != 0:
            continue
        if (timestamp + 17) % 523 != 0:
            continue
        if (timestamp + 7) % 41 != 0:
            continue
        if (timestamp + 54) % 37 != 0:
            continue
        if (timestamp + 77) % 29 != 0:
            print(f"{timestamp:,}")
            continue
        if (timestamp + 40) % 23 != 0:
            continue
        if (timestamp + 36) % 19 != 0:
            continue
        if (timestamp + 35) % 13 != 0:
            continue

        return timestamp
        # if check_timestamp(timestamp, bus_times):
        #     return timestamp

timestamp = get_timestamp()
print("!!!   !!!   !!!")
print(timestamp) # > 133151790670903

