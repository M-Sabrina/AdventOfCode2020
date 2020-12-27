import math

seatcode = "FBFFFFFLLL"

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

seatID = row * 8 + column
print(seatID)
