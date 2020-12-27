import copy
import pprint


def seating_system(contents):
    seats = contents.splitlines()
    seats_array = []
    y_len = len(seats)
    x_len = len(seats[0])
    for y in range(y_len):
        seats_array.append([seats[y][x] for x in range(x_len)])

    seats_array_old = copy.deepcopy(seats_array)

    while True:
        for nrow, row in enumerate(seats_array):
            for ncol, col in enumerate(row):

                if (
                    seats_array_old[nrow][ncol] == "L"
                    or seats_array_old[nrow][ncol] == "#"
                ):
                    around = ""
                    for r in range(nrow - 1, nrow + 2):
                        for c in range(ncol - 1, ncol + 2):
                            # check if not out of range or in center
                            if (
                                c >= 0
                                and r >= 0
                                and c < x_len
                                and r < y_len
                                and not (r == nrow and c == ncol)
                            ):
                                around += seats_array_old[r][c]
                    occupied = around.count("#")
                    # empty = around.count("L")
                    if seats_array_old[nrow][ncol] == "L" and occupied == 0:
                        seats_array[nrow][ncol] = "#"
                    if seats_array_old[nrow][ncol] == "#" and occupied >= 4:
                        seats_array[nrow][ncol] = "L"

        if seats_array == seats_array_old:
            pprint.pprint(seats_array)
            return count_char(seats_array, "#")
        seats_array_old = copy.deepcopy(seats_array)


def count_char(array_2d, char):
    tmp = 0
    for row in array_2d:
        for pos in row:
            if pos == char:
                tmp += 1
    return tmp


def test_tag11():
    contents = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

    solution = seating_system(contents)
    expected = 37
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


# test_tag11()

with open("Tag-11/input.txt", "rt") as myfile:
    contents = myfile.read()

target = seating_system(contents)
print(f"Das Ergebnis von Tag 11 Part 1 ist: {target}")
