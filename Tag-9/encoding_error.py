def encoding_error(contents, preamble):
    numbers_str = contents.split()
    numbers = [int(i) for i in numbers_str]
    errors = list()
    for i, n in enumerate(numbers):
        if i >= preamble:
            found_sum = False
            for first in range(i - preamble, i):
                for second in range(i - preamble + 1, i):
                    if numbers[first] + numbers[second] == n:
                        found_sum = True
            if found_sum is False:
                errors.append(n)

    return errors[0]


def encoding_error_2(contents, target):
    numbers_str = contents.split()
    numbers = [int(i) for i in numbers_str]
    for i, n in enumerate(numbers):
        for first in range(i, len(numbers)):
            for last in range(first + 1, len(numbers)):
                if sum(numbers[first : last + 1]) == target:
                    contiguous = numbers[first : last + 1]
                    print(contiguous)
                    return min(contiguous) + max(contiguous)
    return 0


def test_tag9():
    contents = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

    solution = encoding_error(contents, 5)
    expected = 127
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")

    solution = encoding_error_2(contents, 127)
    expected = 62
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


# test_tag9()

with open("Tag-9/input.txt", "rt") as myfile:
    contents = myfile.read()

target = encoding_error(contents, 25)
print(f"Das Ergebnis von Tag 9 Part 1 ist: {target}")
print(f"Das Ergebnis von Tag 9 Part 2 ist: {encoding_error_2(contents, target)}")
