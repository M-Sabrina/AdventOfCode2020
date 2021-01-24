import numpy as np


def rambunctious_recitation2(contents):
    start_numbers = contents.split(",")
    numbers_array = np.array([int(number) for number in start_numbers])

    turn_dict = {}
    for ind, number in enumerate(numbers_array[:-2]):
        turn_dict[number] = ind

    turn = len(numbers_array) - 1
    last = int(numbers_array[-2])
    new = int(numbers_array[-1])

    while turn < 30000000:
        turn_dict[last] = turn - 1
        if not (new in turn_dict) and (new != last):
            last = new
            new = 0
        elif not (new in turn_dict) and (new == last):
            last = new
            new = 1
        else:
            last = new
            new = turn - turn_dict[new]

        turn += 1

    return last


def test_tag15():
    contents = """\
3,1,2"""
    solution = rambunctious_recitation2(contents)
    expected = 362
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag15()

with open("Tag-15/input.txt", "rt") as myfile:
    contents = myfile.read()

target = rambunctious_recitation2(contents)
print(f"Das Ergebnis von Tag 15 Part 2 ist: {target}")
