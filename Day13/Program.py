
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

    bus_times.append((int(bus), -i % int(bus)))

bus_times.sort()
bus_times.reverse()

i = 0
bus_info = bus_times[0]
bus, offset = bus_info
timestamp = bus + offset
timestamp_increment = bus

for i in range(1, len(bus_times)):
    bus_info = bus_times[i]
    bus, offset = bus_info

    while timestamp % bus != offset:
        timestamp += timestamp_increment

    timestamp_increment *= bus

print(timestamp)
