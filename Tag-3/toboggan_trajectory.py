myfile = open("Tag-3/input.txt", "rt")
contents = myfile.read()
myfile.close()
trees = contents.splitlines()


def check_slope(x_slope, y_slope):
    x_real = 0
    x = 0
    y = 0
    tree_count = 0
    y_length = len(trees)
    x_length = len(trees[0])
    for n in range(int(y_length / y_slope) - 1):
        x_real = x_real + x_slope
        y = y + y_slope
        x = x_real % x_length
        if trees[y][x] == "#":
            tree_count = tree_count + 1
    return tree_count


print(
    check_slope(1, 1)
    * check_slope(3, 1)
    * check_slope(5, 1)
    * check_slope(7, 1)
    * check_slope(1, 2)
)
