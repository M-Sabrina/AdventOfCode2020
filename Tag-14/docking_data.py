import numpy as np


def docking_data(contents):
    lines = contents.splitlines()

    # find length of memory
    max_mem = 0
    for line in lines:
        if line.startswith("mem"):
            mem_str = line[line.find("[") + 1 : line.find("]")]
            mem = int(mem_str)
            if max_mem <= mem:
                max_mem = mem
    memory = np.zeros(max_mem + 1)

    # go through instructions and perform operations
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
            length = len(mask)
        else:
            mem = int(line[line.find("[") + 1 : line.find("]")])
            num = int(line.split(" = ")[1])
            num_bin = bin(num)[2:]
            num_bin_long = ["0" for n in range(length)]
            for n in range(1, len(num_bin) + 1):
                num_bin_long[-n] = num_bin[-n]
            # apply mask
            for n, char in enumerate(mask):
                if char != "X":
                    num_bin_long[n] = mask[n]
            # calculate decimal
            num_new = 0
            for n in range(length):
                num_new += int(num_bin_long[-n - 1]) * (2 ** n)

            # update memory
            memory[mem] = num_new

    # do the math
    return sum(memory)


def test_tag14():
    contents = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

    solution = docking_data(contents)
    expected = 165
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag14()

with open("Tag-14/input.txt", "rt") as myfile:
    contents = myfile.read()

target = docking_data(contents)
print(f"Das Ergebnis von Tag 14 Part 1 ist: {target}")
