import numpy as np


def rambunctious_recitation(contents):
    start_numbers = contents.split(",")
    numbers = np.array([int(number) for number in start_numbers])

    while len(numbers) < 2020:
        last = numbers[-1]
        count = np.count_nonzero(numbers == last)

        if count == 1:
            numbers = np.append(numbers, [0])
        else:
            diff = np.where(numbers == last)[0][-1] - np.where(numbers == last)[0][-2]
            numbers = np.append(numbers, [diff])

    return numbers[-1]


def test_tag15():
    contents = """\
3,1,2"""
    solution = rambunctious_recitation(contents)
    expected = 1836
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag15()

with open("Tag-15/input.txt", "rt") as myfile:
    contents = myfile.read()

target = rambunctious_recitation(contents)
print(f"Das Ergebnis von Tag 15 Part 1 ist: {target}")
