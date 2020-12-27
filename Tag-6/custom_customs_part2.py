import numpy as np

with open("Tag-6/input.txt", "rt") as myfile:
    contents = myfile.read()

groups = contents.split("\n\n")

while "" in groups:
    groups.remove("")

answers_per_group = np.zeros(len(groups))

for n, group in enumerate(groups):
    people = group.split("\n")
    people_set = set(people[0])
    for i, person in enumerate(people):
        if i > 0:
            temp_set = people_set.intersection(set(person))
            people_set = temp_set
    answers_per_group[n] = len(people_set)

print(sum(answers_per_group))
