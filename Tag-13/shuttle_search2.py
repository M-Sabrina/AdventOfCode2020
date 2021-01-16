import numpy as np

# brute force: test works, but real thing runs for ever and ever and ...
# def shuttle_search2(contents):
#    notes = contents.splitlines()
#    lines_list = notes[1].split(",")
#    lines = np.array([int(i) if i != "x" else 0 for i in lines_list])
#    n = 1
#    found = False
#    while True:
#        t = n * lines[0]
#        tmp = 1
#        for line in lines[1:]:
#            if line == 0:
#                tmp += 1
#            elif np.mod(t + tmp, line) == 0:
#                tmp += 1
#                if line == lines[-1]:
#                    found = True
#            else:
#                break
#
#        if found is True:
#            return t
#        else:
#            n += 1

# smart version with help from the outside world (thanks outside world!)
def shuttle_search2(contents):
    notes = contents.splitlines()
    lines_list = notes[1].split(",")
    lines = np.array([int(i) if i != "x" else 0 for i in lines_list])
    time = 0
    skip = 0
    product = lines[0]
    for index, bus in enumerate(lines[:-1]):

        skip = 0
        next = lines[index + 1]

        while next == 0:
            skip += 1
            next = lines[index + 1 + skip]

        if bus != 0:
            while (time + index + 1 + skip) % next != 0:
                time += product

            product *= next

    return time


def test_tag13():
    contents = """\
939
7,13,x,x,59,x,31,19"""

    solution = shuttle_search2(contents)
    expected = 1068781
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag13()

with open("Tag-13/input.txt", "rt") as myfile:
    contents = myfile.read()

target = shuttle_search2(contents)
print(f"Das Ergebnis von Tag 13 Part 2 ist: {target}")
