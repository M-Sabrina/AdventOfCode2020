def handy_haversacks_2(contents):
    rules = contents.splitlines()
    rules_dict = {}

    for i, rule in enumerate(rules):
        outer_bag = rule.split(" contain ")[0]
        inner_bags = ((rule.split(" contain ")[1])[:-1]).split(", ")
        temp_dict = {}
        for n, inner_bag in enumerate(inner_bags):
            if inner_bag != "no other bags":
                if inner_bag[-1] != "s":  # bag
                    temp_dict[inner_bag[2:] + "s"] = inner_bag[0]
                else:  # bags
                    temp_dict[inner_bag[2:]] = inner_bag[0]
        rules_dict[outer_bag] = temp_dict

    inner_bags = list()

    for entry in rules_dict["shiny gold bags"]:
        for n in range(int(rules_dict["shiny gold bags"][entry])):
            inner_bags.append(entry)

    new_inner_bags = list()
    new_inner_bags = inner_bags.copy()

    count = len(inner_bags)

    while True:
        for bag in inner_bags:
            for entry in rules_dict:
                if bag == entry:
                    new_inner_bags.remove(entry)
                    for subentry in rules_dict[entry]:
                        for n in range(int(rules_dict[entry][subentry])):
                            new_inner_bags.append(subentry)
                            count += 1
        if new_inner_bags == inner_bags:
            break
        else:
            inner_bags = new_inner_bags.copy()

    return count


def test_tag7_2():
    contents = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

    solution = handy_haversacks_2(contents)
    expected = 126
    if solution != expected:
        print("--------------FEHLER---------------------------------------")
        print(f" Das Ergebnis des Tests ist {solution} und nicht {expected}")


test_tag7_2()

with open("Tag-7/input.txt", "rt") as myfile:
    contents = myfile.read()

print(f"Das Ergebnis von Tag 7 Part 2 ist: {handy_haversacks_2(contents)}")
