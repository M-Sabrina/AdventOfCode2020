from math import sin
from math import cos
from math import radians


def rain_risk(contents):
    instructions = contents.splitlines()
    # east := 0 degree
    angle = 0
    y = 0  # positive = north, negative = south
    x = 0  # positive = east, negative = west
    for instruction in instructions:
        direction = instruction[0]
        value = int(instruction[1:])
        if direction == "N":
            y += value
        if direction == "S":
            y -= value
        if direction == "E":
            x += value
        if direction == "W":
            x -= value
        if direction == "L":
            angle += value
        if direction == "R":
            angle -= value
        if direction == "F":
            y += value * sin(radians(angle))
            x += value * cos(radians(angle))

    # Manhattan distance
    return abs(x) + abs(y)


def test_tag12():
    contents = """\
F10
N3
F7
R90
F11"""

    solution = rain_risk(contents)
    expected = 25
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag12()

with open("Tag-12/input.txt", "rt") as myfile:
    contents = myfile.read()

target = rain_risk(contents)
print(f"Das Ergebnis von Tag 12 Part 1 ist: {target}")
