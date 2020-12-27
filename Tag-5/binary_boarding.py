import math
import numpy as np

with open("Tag-5/input.txt", "rt") as myfile:
    contents = myfile.read()

seats = contents.splitlines()

# part 1

seatIDs = np.zeros(len(seats))
for n, seatcode in enumerate(seats):

    row_string = seatcode[0:8]
    max = 127
    min = 0
    for c in row_string:
        if c == "F":
            max = math.floor(max - (max - min) / 2)
        if c == "B":
            min = math.ceil(min + (max - min) / 2)
    row = max

    column_string = seatcode[7:]
    max = 7
    min = 0
    for c in column_string:
        if c == "L":
            max = math.floor(max - (max - min) / 2)
        if c == "R":
            min = math.ceil(min + (max - min) / 2)
    column = max

    seatIDs[n] = row * 8 + column

np_seatIDs = np.array(seatIDs)
print(np.max(np_seatIDs))

# part 2

sorted_seatIDs = np.sort(np_seatIDs)

first_seat = sorted_seatIDs[0]
offset = 0

for n, seat in enumerate(sorted_seatIDs):
    if not (seat == (n + offset + first_seat)):
        print(seat - 1)
        offset += 1
