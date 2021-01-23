def docking_data2(contents):

    lines = contents.splitlines()

    memory = {}

    # go through instructions and perform operations
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
            length = len(mask)
        else:
            mem = int(line[line.find("[") + 1 : line.find("]")])
            num = int(line.split(" = ")[1])

            mem_bin = bin(mem)[2:]
            mem_bin_long = ["0" for n in range(length)]
            for n in range(1, len(mem_bin) + 1):
                mem_bin_long[-n] = mem_bin[-n]

            # apply mask and count Xs
            xcount = 0
            for n, char in enumerate(mask):
                if (char == "X") or (char == "1"):
                    mem_bin_long[n] = mask[n]
                if char == "X":
                    xcount += 1

            # go through all possible memory positions
            for n in range(2 ** xcount):
                n_bin = bin(n)[2:]

                # fill up missing leading zeros
                while len(n_bin) < xcount:
                    n_bin = "0" + n_bin

                mem_bin_long_tmp = mem_bin_long.copy()

                # replace X by binary position p
                for p in n_bin:
                    for i, char in enumerate(mem_bin_long_tmp):
                        if char == "X":
                            mem_bin_long_tmp[i] = p
                            break

                # decimal conversion
                mem_new = 0
                for i in range(length):
                    mem_new += int(mem_bin_long_tmp[-i - 1]) * (2 ** i)

                # update memory
                memory[mem_new] = num

    # do the math
    sum = 0
    for entry in memory:
        sum += memory[entry]
    return sum


def test_tag14():
    contents = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

    solution = docking_data2(contents)
    expected = 208
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag14()

with open("Tag-14/input.txt", "rt") as myfile:
    contents = myfile.read()

target = docking_data2(contents)
print(f"Das Ergebnis von Tag 14 Part 2 ist: {target}")
