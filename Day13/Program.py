
timestampStr, busesStr = open('Day13\input.txt').read().split('\n')
timestamp = int(timestampStr)
buses = [int(bus) for bus in busesStr.split(',') if bus != 'x']
buses_after_timestamp = [((int(timestamp / bus) + 1) * bus, bus) for bus in buses]
bus_timestamp, bus = min(buses_after_timestamp)
print(bus * (bus_timestamp - timestamp))
