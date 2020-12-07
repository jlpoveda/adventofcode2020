import re

with open("./aoc05.txt") as file:
    input = list(file.read().splitlines())

max_seat_id = 0
seats = []
for seat in input:
    s = seat.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
    seat_id = int(s[0:7], 2) * 8 + int(s[7:10], 2)
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    seats.append(seat_id)
    seats = sorted(seats)

print("Max seat_id", max_seat_id)


old_s = seats[0] - 1
for s in seats:
    if old_s + 1 == s:
        old_s = s
        continue
    else:
        print("My seat", s - 1)
        break




