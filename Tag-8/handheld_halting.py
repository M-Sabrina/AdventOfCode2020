import numpy as np


def handheld_halting(contents):
    instructions = contents.splitlines()
    accumulator = 0
    n = 0
    check = np.zeros(len(instructions))
    while True:
        if check[n] == 1:
            break
        check[n] = 1
        line = instructions[n]
        instruction = line.split(" ")[0]
        number = int(line.split(" ")[1])
        if instruction == "acc":
            accumulator += number
            n += 1
        elif instruction == "nop":
            n += 1
        elif instruction == "jmp":
            n += number

    return accumulator


def test_tag8():
    contents = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

    solution = handheld_halting(contents)
    expected = 5
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag8()

with open("Tag-8/input.txt", "rt") as myfile:
    contents = myfile.read()

print(f"Das Ergebnis von Tag 8 ist: {handheld_halting(contents)}")
