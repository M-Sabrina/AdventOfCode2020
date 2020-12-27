import numpy as np

myfile = open("Tag-4/input.txt", "rt")
contents = myfile.read()
myfile.close()

passports = contents.split("\n\n")
valid_passports = np.zeros(len(passports))
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# part 1

for n, data in enumerate(passports):
    valid = 1
    for f in fields:
        if not (f in data):
            valid = 0
    valid_passports[n] = valid

print(sum(valid_passports))

# part 2

for i, n in enumerate(valid_passports):
    valid = 1
    if n == 1:
        check_passport = (passports[i].replace("\n", " ")).split(" ")
        check_dict = {}
        for item in check_passport:
            if ":" in item:
                check_dict[(item.split(":"))[0]] = (item.split(":"))[1]

        # now all entries in check_dict
        byr = check_dict["byr"]
        iyr = check_dict["iyr"]
        eyr = check_dict["eyr"]
        hgt = check_dict["hgt"]
        hcl = check_dict["hcl"]
        ecl = check_dict["ecl"]
        pid = check_dict["pid"]

        # now check all criteria

        if not (len(byr) == 4 and len(iyr) == 4 and len(eyr) == 4):
            valid = 0

        if not (int(byr) >= 1920 and int(byr) <= 2002):
            valid = 0

        if not (int(iyr) >= 2010 and int(iyr) <= 2020):
            valid = 0

        if not (int(eyr) >= 2020 and int(eyr) <= 2030):
            valid = 0

        if not (hgt[-2:] == "cm" or hgt[-2:] == "in"):
            valid = 0

        if hgt[-2:] == "cm":
            if not (float(hgt[:-2]) >= 150 and float(hgt[:-2]) <= 193):
                valid = 0

        if hgt[-2:] == "in":
            if not (float(hgt[:-2]) >= 59 and float(hgt[:-2]) <= 76):
                valid = 0

        if not (hcl[0] == "#" and len(hcl) == 7):
            valid = 0

        for c in hcl[1:]:
            if not (
                (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 97 and ord(c) <= 102)
            ):
                valid = 0

        if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            valid = 0

        if not (len(pid) == 9):
            valid = 0
        for c in pid:
            if not (ord(c) >= 48 and ord(c) <= 57):
                valid = 0

        # last, re-evaluate
        valid_passports[i] = valid

print(sum(valid_passports))
