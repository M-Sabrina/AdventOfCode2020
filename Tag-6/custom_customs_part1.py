import numpy as np

with open("Tag-6/input.txt", "rt") as myfile:
    contents = myfile.read()

groups_newline = contents.split("\n\n")
groups = [""]

for group in groups_newline:
    groups.append(group.replace("\n", ""))

while "" in groups:
    groups.remove("")

answers_per_group = np.zeros(len(groups))

for i, group in enumerate(groups):
    letters_set = set()
    for c in group:
        letters_set.add(c)
    answers_per_group[i] = len(letters_set)

print(sum(answers_per_group))
