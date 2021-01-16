import numpy as np


def shuttle_search(contents):
    notes = contents.splitlines()
    now = int(notes[0])
    lines_list = notes[1].split(",")
    lines = np.array([int(i) for i in lines_list if i != "x"])
    waiting_times = np.array([-np.mod(now, line) + line for line in lines])
    wait = min(waiting_times)
    next_line = lines[np.where(waiting_times == min(waiting_times))]
    return int(wait * next_line)


def test_tag13():
    contents = """\
939
7,13,x,x,59,x,31,19"""

    solution = shuttle_search(contents)
    expected = 295
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag13()

with open("Tag-13/input.txt", "rt") as myfile:
    contents = myfile.read()

target = shuttle_search(contents)
print(f"Das Ergebnis von Tag 13 Part 1 ist: {target}")
