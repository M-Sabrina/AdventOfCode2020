myfile = open("Tag-2/input.txt", "rt")  # open input.txt for reading text
contents = myfile.read()  # read the entire file to string
myfile.close()  # close the file

passwords = contents.splitlines()
length = len(passwords)

valid_count = 0

for l in range(length):
    pos1 = int(((passwords[l].split(" "))[0]).split("-")[0]) - 1
    pos2 = int(((passwords[l].split(" "))[0]).split("-")[1]) - 1
    letter = ((passwords[l].split(" "))[1])[0]
    pw = (passwords[l].split(" "))[2]
    count = 0
    if pw[pos1] == letter:
        count = count + 1
    if pw[pos2] == letter:
        count = count + 1
    if count == 1:
        valid_count = valid_count + 1

print(str(valid_count))