import numpy as np


def handheld_halting_2(contents):
    instructions = contents.splitlines()

    for index, instr in enumerate(instructions):

        command = instr.split(" ")[0]

        if command == "acc":
            pass

        else:

            accumulator = 0
            n = 0
            check = np.zeros(len(instructions))
            max_n = len(instructions)
            completed = False

            while True:
                if n == max_n:
                    completed = True
                    break
                if check[n] == 1:
                    break
                check[n] = 1
                line = instructions[n]
                instruction = line.split(" ")[0]
                number = int(line.split(" ")[1])

                # for the particular line where we exchance the command, switch:
                if n == index:
                    if instruction == "jmp":
                        instruction = "nop"
                    elif instruction == "nop":
                        instruction = "jmp"

                if instruction == "acc":
                    accumulator += number
                    n += 1
                elif instruction == "nop":
                    n += 1
                elif instruction == "jmp":
                    n += number

        if completed is True:
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

    solution = handheld_halting_2(contents)
    expected = 8
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag8()

with open("Tag-8/input.txt", "rt") as myfile:
    contents = myfile.read()

print(f"Das Ergebnis von Tag 8 ist: {handheld_halting_2(contents)}")
