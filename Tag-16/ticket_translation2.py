import numpy as np

# 	3	9	18
# ____________
# c 0	1	1

# r	1	1	1

# s	1	1	1

# A --> c is not pos 0


# 	15	1	5
# ____________
# c	1	1	1

# r	1	1	1

# s	0	1	1

# B --> s is not pos 0


# 	5	14	9
# ____________
# c	1	1	1

# r	1	1	1

# s	1	0	1

# C --> s is not pos 1


# AND matrix

#   0   1   2
# ____________
# c 0	1	1       2

# r	1	1	1       3

# s	0	0	1       1

# 	B, C --> s is pos 2
# 	A --> c is pos 1
# 	--> r is pos 0


def ticket_translation2(contents):
    notes = contents.split("\n\n")
    fields = notes[0].splitlines()
    ticket = notes[1].splitlines()[1]
    nearby = notes[2].splitlines()[1:]

    field_names = list()
    field_ranges = list()
    for i, field in enumerate(fields):
        field_names.append(field.split(": ")[0])
        range_1_str = field.split(": ")[1].split(" or ")[0]
        range_2_str = field.split(": ")[1].split(" or ")[1]
        range_1_min = int(range_1_str.split("-")[0])
        range_1_max = int(range_1_str.split("-")[1]) + 1
        range_2_min = int(range_2_str.split("-")[0])
        range_2_max = int(range_2_str.split("-")[1]) + 1
        field_range_tmp = set()
        for n in range(range_1_min, range_1_max):
            field_range_tmp.add(n)
        for n in range(range_2_min, range_2_max):
            field_range_tmp.add(n)
        field_ranges.append(field_range_tmp.copy())

    x_dim = len(fields)
    y_dim = len(nearby)

    valid_check = np.zeros(y_dim, np.int)

    y_dim = 0

    for i, nearby_ticket in enumerate(nearby):

        # discard invalid nearby tickets
        ticket_check = True
        for p in range(x_dim):
            tmp = int(nearby_ticket.split(",")[p])
            check_tmp = False
            for n in range(x_dim):
                if tmp in field_ranges[n]:
                    check_tmp = True
            if check_tmp is False:
                ticket_check = False

        if ticket_check is True:
            valid_check[i] = 1
            y_dim += 1

    nearby_array = np.zeros((y_dim, x_dim))

    y_count = -1
    for y, n in enumerate(valid_check):
        if n == 1:
            y_count += 1
            for x in range(x_dim):
                nearby_array[(y_count, x)] = int((nearby[y].split(","))[x])

    # now nearby_array contains all potentially valid tickets in np.array
    # print(nearby_array)

    # now follow matrix strategy described above

    and_matrix = np.ones((x_dim, x_dim))

    for seat in nearby_array:
        tmp_matrix = np.zeros((x_dim, x_dim))
        for n, s in enumerate(seat):
            for f, field_range in enumerate(field_ranges):
                if s in field_range:
                    tmp_matrix[(f, n)] = 1
        and_matrix = np.logical_and(and_matrix, tmp_matrix)

    # now do assignment of position <--> field

    and_matrix_sum = np.zeros(x_dim)

    for n, nearby_seat in enumerate(and_matrix):
        and_matrix_sum[n] = sum(nearby_seat)

    pos_occupied = np.zeros(x_dim)

    field_position = np.zeros(x_dim)

    count = 1
    while count <= x_dim:
        ind = np.where(and_matrix_sum == count)
        index = int(ind[0])
        and_matrix_line = and_matrix[index]
        for p, pos in enumerate(and_matrix_line):
            if pos_occupied[p] == 1:
                and_matrix_line[p] = False
        found_pos = np.where(and_matrix_line == 1)
        found_position = int(found_pos[0])
        pos_occupied[found_position] = 1
        field_position[index] = found_position
        count += 1

    # output to console
    print(field_names)
    print(field_position)

    # look for fields starting with departure
    ticket_numbers = np.zeros(x_dim)
    for x in range(x_dim):
        ticket_numbers[x] = ticket.split(",")[x]
    result = 1
    for n, field_name in enumerate(field_names):
        if field_name.startswith("departure"):
            pos = int(field_position[n])
            result *= ticket_numbers[pos]
    return result


def test_tag16():
    contents = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
    print(" The order of the fields is:")
    ticket_translation2(contents)
    print(" It should be: [1, 0, 2]")


test_tag16()

with open("Tag-16/input.txt", "rt") as myfile:
    contents = myfile.read()

target = ticket_translation2(contents)
print(f"Das Ergebnis von Tag 16 Part 2 ist: {target}")
