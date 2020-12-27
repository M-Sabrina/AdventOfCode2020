import numpy as np

numbers = np.array(np.loadtxt("Tag-1/input.txt"))

a = 0
b = 0
c = 0

for m in numbers:
    for n in numbers:
        for o in numbers:
            if (m + n + o) == 2020:
                a = m
                b = n
                c = o

print(a * b * c)