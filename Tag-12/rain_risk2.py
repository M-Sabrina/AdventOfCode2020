from math import sin
from math import asin
from math import cos
from math import radians
from math import sqrt
from numpy import pi as pi


def rain_risk2(contents):
    instructions = contents.splitlines()

    # ship's coordinates:
    y = 0  # positive = north, negative = south
    x = 0  # positive = east, negative = west

    # waypoint's coordiantes, relative to ship:
    y_wp = 1
    x_wp = 10

    for instruction in instructions:

        direction = instruction[0]
        value = int(instruction[1:])

        if direction == "N":
            y_wp += value
        if direction == "S":
            y_wp -= value
        if direction == "E":
            x_wp += value
        if direction == "W":
            x_wp -= value

        if direction == "L" or direction == "R":

            distance = sqrt(x_wp ** 2 + y_wp ** 2)

            # below: angle in rad
            if y_wp >= 0 and x_wp >= 0:
                angle = asin(abs(y_wp) / distance)
            elif y_wp >= 0 and x_wp <= 0:
                angle = pi - asin(abs(y_wp) / distance)
            elif y_wp <= 0 and x_wp >= 0:
                angle = 2 * pi - asin(abs(y_wp) / distance)
            elif y_wp <= 0 and x_wp <= 0:
                angle = pi + asin(abs(y_wp) / distance)

            if direction == "L":
                angle += radians(value)
            if direction == "R":
                angle -= radians(value)

            y_wp = distance * sin(angle)
            x_wp = distance * cos(angle)

        if direction == "F":
            y += value * y_wp
            x += value * x_wp

    # Manhattan distance
    return abs(x) + abs(y)


def test_tag12():
    contents = """\
F10
N3
F7
R90
F11"""

    solution = rain_risk2(contents)
    expected = 286
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag12()

with open("Tag-12/input.txt", "rt") as myfile:
    contents = myfile.read()

target = rain_risk2(contents)
print(f"Das Ergebnis von Tag 12 Part 2 ist: {target}")
