# https://adventofcode.com/2020/day/12

def shuttle_search():
    f = open("input.txt").read().splitlines()
    depart = int(f[0])
    buses = {int(bus):int(bus) - depart % int(bus) for bus in f[1].split(",")
             if bus != "x"}
    earliest_bus_id = min(buses, key=buses.get)
    return earliest_bus_id*buses[earliest_bus_id]


def shuttle_search_second():
    f = open("input.txt").read().splitlines()
    buses = {int(bus):int(bus) - depart % int(bus) for bus in f[1].split(",")}
    earliest_bus_id = min(buses, key=buses.get)
    return earliest_bus_id*buses[earliest_bus_id]


print(shuttle_search())