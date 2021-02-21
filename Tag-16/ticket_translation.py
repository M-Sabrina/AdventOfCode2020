def ticket_translation(contents):
    notes = contents.split("\n\n")
    fields = notes[0].splitlines()
    # ticket = notes[1].splitlines()[1]
    nearby = notes[2].splitlines()[1:]

    valid = set()

    for field in fields:
        valid_ranges = field.split(": ")[1]
        for i in range(2):
            valid_range = valid_ranges.split(" or ")[i]
            min = int(valid_range.split("-")[0])
            max = int(valid_range.split("-")[1]) + 1
            for n in range(min, max):
                valid.add(n)

    invalid = list()

    for line in nearby:
        numbers = line.split(",")
        for number in numbers:
            if not (int(number) in valid):
                invalid.append(int(number))

    return sum(invalid)


def test_tag16():
    contents = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    solution = ticket_translation(contents)
    expected = 71
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag16()

with open("Tag-16/input.txt", "rt") as myfile:
    contents = myfile.read()

target = ticket_translation(contents)
print(f"Das Ergebnis von Tag 16 Part 1 ist: {target}")
