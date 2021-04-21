# https://adventofcode.com/2020/day/12

directions = ['E', 'S', 'W', 'N']


def move(direction, x, y, val):
    """Move the object in input direction and value"""
    if direction == 'N':
        y += val
    elif direction == 'S':
        y -= val
    elif direction == 'W':
        x -= val
    elif direction == 'E':
        x += val
    return x, y

def rain_risk():
    """Find the Manhattan distance between location and the ship's starting
    position with input instructions.
    """
    x = y = 0
    facing = 'E'
    for line in open("input.txt").read().splitlines():
        action, val = line[0], int(line[1:])
        if action in directions:
            x, y = move(action, x, y, val)
        if action == 'F':
            x, y = move(facing, x, y, val)
        elif action == 'R':
            current_dir = directions.index(facing)
            val /= 90
            facing = directions[int((current_dir + val) % 4)]
        elif action == 'L':
            current_dir = directions.index(facing)
            val /= 90
            facing = directions[int((current_dir - val) % 4)]
    return abs(x) + abs(y)


def rain_risk_second():
    """Find the Manhattan distance between location and the ship's starting
    position with input instructions that indicate how to move a waypoint.
    """
    x = 0
    y = 0
    wx = 10
    wy = 1
    for line in open("input.txt").read().splitlines():
        action, val = line[0], int(line[1:])
        if action in directions:
            wx, wy = move(action, wx, wy, val)
        if action == 'F':
            for i in range(val):
                x += wx
                y += wy
        elif action == 'R':
            val /= 90
            for i in range(int(val)):
                wx, wy = wy, -wx
        elif action == 'L':
            val /= 90
            for i in range(int(val)):
                wx, wy = -wy, wx
    distance = abs(x) + abs(y)
    return distance


print(rain_risk())
print(rain_risk_second())