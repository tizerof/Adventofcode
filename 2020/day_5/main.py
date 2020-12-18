# https://adventofcode.com/2020/day/5


def find_my_seat_first(file_name):
    max_seat_id = 0
    for seat in  open(file_name).readlines():
        row = sum([num*(2**i) for i,num in enumerate([1 if row == "B" else 0 for row in seat[:7]][::-1])])
        column = sum([num*(2**i) for i,num in enumerate([1 if row == "R" else 0 for row in seat[7:10]][::-1])])
        seat_id = row * 8 + column
        if max_seat_id < seat_id:
            max_seat_id = seat_id
    return max_seat_id


def find_my_seat_second(file_name):
    seats = []
    for seat in  open(file_name).readlines():
        row = sum([num*(2**i) for i,num in enumerate([1 if row == "B" else 0 for row in seat[:7]][::-1])])
        column = sum([num*(2**i) for i,num in enumerate([1 if row == "R" else 0 for row in seat[7:10]][::-1])])
        seats.append(row * 8 + column)
    seats.sort()
    print(seats)
    for i in range(1, len(seats)):
        if seats[i] != seats[i-1]+1:
            return seats[i] - 1


print(find_my_seat_first("input.txt"))
print(find_my_seat_second("input.txt"))