import numpy as np


def adapter_array2(contents):
    numbers_str = contents.split()
    numbers_long = [int(i) for i in numbers_str]
    numbers_long.append(0)
    numbers_long.append(max(numbers_long) + 3)
    numbers_set = set(numbers_long)
    numbers_np_unsorted = np.array(numbers_long)
    numbers_np = np.sort(numbers_np_unsorted)
    count_np = np.zeros(len(numbers_np))
    count_np[0] = 1

    for i in range(1, len(numbers_np)):
        n = numbers_np[i]
        for c in range(1, 4):
            if (n - c) in numbers_set:
                index = np.where(numbers_np == (n - c))
                count_np[i] += count_np[index]

    return count_np[-1]


def test_tag10():
    contents = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

    solution = adapter_array2(contents)
    expected = 19208
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag10()

with open("Tag-10/input.txt", "rt") as myfile:
    contents = myfile.read()

target = adapter_array2(contents)
print(f"Das Ergebnis von Tag 10 Part 2 ist: {target}")
