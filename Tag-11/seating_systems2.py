import copy
import pprint


def seating_system2(contents):
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

                    # west (left)
                    if ncol > 0:
                        for c in range(ncol - 1, -1, -1):
                            if (
                                seats_array_old[nrow][c] == "L"
                                or seats_array_old[nrow][c] == "#"
                            ):
                                around += seats_array_old[nrow][c]
                                break

                    # east (right)
                    if ncol < x_len - 1:
                        for c in range(ncol + 1, x_len):
                            if (
                                seats_array_old[nrow][c] == "L"
                                or seats_array_old[nrow][c] == "#"
                            ):
                                around += seats_array_old[nrow][c]
                                break

                    # south (down)
                    if nrow < y_len - 1:
                        for r in range(nrow + 1, y_len):
                            if (
                                seats_array_old[r][ncol] == "L"
                                or seats_array_old[r][ncol] == "#"
                            ):
                                around += seats_array_old[r][ncol]
                                break

                    # north (up)
                    if nrow > 0:
                        for r in range(nrow - 1, -1, -1):
                            if (
                                seats_array_old[r][ncol] == "L"
                                or seats_array_old[r][ncol] == "#"
                            ):
                                around += seats_array_old[r][ncol]
                                break

                    # southwest (left down diagonal)
                    if nrow < y_len - 1 and ncol > 0:
                        r = nrow
                        c = ncol
                        while (r < y_len - 1) and (c > 0):
                            r += 1
                            c -= 1
                            if (
                                seats_array_old[r][c] == "L"
                                or seats_array_old[r][c] == "#"
                            ):
                                around += seats_array_old[r][c]
                                break

                    # southeast (right down diagonal)
                    if nrow < y_len - 1 and ncol < x_len - 1:
                        r = nrow
                        c = ncol
                        while (r < y_len - 1) and (c < x_len - 1):
                            r += 1
                            c += 1
                            if (
                                seats_array_old[r][c] == "L"
                                or seats_array_old[r][c] == "#"
                            ):
                                around += seats_array_old[r][c]
                                break

                    # northwest (left up diagonal)
                    if nrow > 0 and ncol > 0:
                        r = nrow
                        c = ncol
                        while (r > 0) and (c > 0):
                            r -= 1
                            c -= 1
                            if (
                                seats_array_old[r][c] == "L"
                                or seats_array_old[r][c] == "#"
                            ):
                                around += seats_array_old[r][c]
                                break

                    # northeast (right up diagonal)
                    if nrow > 0 and ncol < x_len - 1:
                        r = nrow
                        c = ncol
                        while (r > 0) and (c < x_len - 1):
                            r -= 1
                            c += 1
                            if (
                                seats_array_old[r][c] == "L"
                                or seats_array_old[r][c] == "#"
                            ):
                                around += seats_array_old[r][c]
                                break

                    occupied = around.count("#")

                    if seats_array_old[nrow][ncol] == "L" and occupied == 0:
                        seats_array[nrow][ncol] = "#"
                    if seats_array_old[nrow][ncol] == "#" and occupied >= 5:
                        seats_array[nrow][ncol] = "L"

        if seats_array == seats_array_old:
            pprint.pprint(seats_array)
            return count_char(seats_array, "#")
        else:
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

    solution = seating_system2(contents)
    expected = 26
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag11()

with open("Tag-11/input.txt", "rt") as myfile:
    contents = myfile.read()

target = seating_system2(contents)
print(f"Das Ergebnis von Tag 11 Part 2 ist: {target}")
