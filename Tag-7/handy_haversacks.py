import numpy as np


def handy_haversacks(contents):
    rules = contents.splitlines()
    rules_dict = {}

    for i, rule in enumerate(rules):
        outer_bag = rule.split(" contain ")[0]
        inner_bags = ((rule.split(" contain ")[1])[0:-1]).split(", ")
        temp_dict = {}
        for n, inner_bag in enumerate(inner_bags):
            if inner_bag[-3] == "b":  # bag
                temp_dict[inner_bag[2:] + "s"] = inner_bag[0]
            else:  # bags
                temp_dict[inner_bag[2:]] = inner_bag[0]
        rules_dict[outer_bag] = temp_dict

    outer_bags = set()

    for entry in rules_dict:
        for subentry in rules_dict[entry]:
            if subentry.startswith("shiny gold bag"):
                outer_bags.add(entry)

    new_outer_bags = set()
    new_outer_bags = outer_bags.copy()

    while True:
        for bag in outer_bags:
            containers = set()
            for entry in rules_dict:
                for subentry in rules_dict[entry]:
                    if subentry.startswith(bag):
                        containers.add(entry)
            if len(containers) > 0:
                # new_outer_bags.remove(bag)
                new_outer_bags.update(containers)

        if new_outer_bags == outer_bags:
            break
        else:
            outer_bags = new_outer_bags.copy()

    return len(outer_bags)


def test_tag7():
    contents = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

    solution = handy_haversacks(contents)
    expected = 4
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag7()

with open("Tag-7/input.txt", "rt") as myfile:
    contents = myfile.read()


print(f"Das Ergebnis von Tag 7 ist: {handy_haversacks(contents)}")
