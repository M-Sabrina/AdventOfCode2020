def adapter_array(contents):
    numbers_str = contents.split()
    numbers = set([int(i) for i in numbers_str])
    one_jolt_diff = 0
    two_jolt_diff = 0
    three_jolt_diff = 0
    output = 0
    while len(numbers) > 0:
        output += 1
        if output in numbers:
            numbers.remove(output)
            one_jolt_diff += 1
        else:
            output += 1
            if output in numbers:
                numbers.remove(output)
                two_jolt_diff += 1
            else:
                output += 1
                numbers.remove(output)
                three_jolt_diff += 1

    three_jolt_diff += 1
    print(
        f"one jolt: {one_jolt_diff}, two jolt: {two_jolt_diff}, three jolt: {three_jolt_diff}"
    )
    return one_jolt_diff * three_jolt_diff


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

    solution = adapter_array(contents)
    expected = 220
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


# test_tag10()

with open("Tag-10/input.txt", "rt") as myfile:
    contents = myfile.read()

target = adapter_array(contents)
print(f"Das Ergebnis von Tag 10 Part 1 ist: {target}")
