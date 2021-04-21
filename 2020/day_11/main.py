# https://adventofcode.com/2020/day/11


def apply_rules_seat(nearby_seats, seat, max):
    """ Checks seating conditions based on nearby seats """
    if seat == "L" and "#" not in nearby_seats:
            return "#"
    if seat == "#" and nearby_seats.count("#") >= max:
            return "L"
    return seat


def apply_rules_row(row, top_row=None, bottom_row=None):
    """ Create new row based on simple rule for row with 8 nearby seats """
    new_row = ""
    if not top_row:
        top_row = "." * len(row)
    if not bottom_row:
        bottom_row = "." * len(row)
    row = "." + row + "."
    top_row = "." + top_row + "."
    bottom_row = "." + bottom_row + "."
    for i, seat in enumerate(row[1:-1]):
        nearby_seats = (top_row[i:i+3] + bottom_row[i:i+3] + row[i] + row[i+2])
        new_row += apply_rules_seat(nearby_seats, seat, 4)
    return new_row


def model_people():
    """ Simulates the seating of people
    according to simple rules sitting nearby.
    """
    layout = open("input.txt").read().splitlines()
    count_occupied_seats = 0
    while True:
        layout_new = []
        for i, row in enumerate(layout):
            if i == 0:
                layout_new.append(apply_rules_row(row=row,
                                                  bottom_row=layout[1]))
            elif i == len(layout)-1:
                layout_new.append(apply_rules_row(row=row, top_row=layout[-2]))
            else:
                layout_new.append(apply_rules_row(row=row, top_row=layout[i-1],
                                                  bottom_row=layout[i+1]))
        count_seats = sum([seats.count("#") for seats in layout_new])
        if count_occupied_seats == count_seats:
            return count_occupied_seats
        else:
            count_occupied_seats = count_seats
        layout = layout_new


print(model_people())

""" PART 2 """


def model_people_second():
    """ Simulates the seating of people according to
    rules sitting visibility in in each eight directions.
    """
    layout = open("input.txt").read().splitlines()
    count_occupied_seats = 0
    while True:
        layout_new = []
        for row in range(len(layout)):
            new_row = ''
            for col in range(len(layout[0])):
                visible_seats = ""
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if x == y == 0:
                            continue
                        i = 1
                        while (0 <= row+i*x < len(layout) and
                               0 <= col+i*y < len(layout[0])):
                            seat = layout[row+i*x][col+i*y]
                            if seat != '.':
                                visible_seats += seat
                                break
                            i += 1
                new_row += apply_rules_seat(visible_seats, layout[row][col], 5)
            layout_new.append(new_row)
        count_seats = sum([seats.count("#") for seats in layout_new])
        if count_occupied_seats == count_seats:
            return count_occupied_seats
        else:
            count_occupied_seats = count_seats
        layout = layout_new


print(model_people_second())
