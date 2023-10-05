# Part 2 (In Progress):

import re

byr_valid = lambda year: 1920 <= year <= 2002
iyr_valid = lambda year: 2010 <= year <= 2020
eyr_valid = lambda year: 2020 <= year <= 2030
ecl_valid = lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'hzl', 'oth']
pid_valid = lambda pid: len(pid) == 9
hcl_valid = lambda hcl: re.match('^#[a-f0-9]{6}$', hcl)
def hgt_valid(input):
    return(
        (59 <= int(input.replace('in', '')) <= 76) if 'in' in input else
        (150 <= int(input.replace('in', '')) <= 189) if 'cm' in input else
        False
    )

def verify(passport):
    fields = [re.search(r'byr:(\w+\d+)', passport),
              re.search(r'iyr:(\w+\d+)', passport),
              re.search(r'eyr:(\w+\d+)', passport),
              re.search(r'ecl:(\w+\d+)', passport),
              re.search(r'pid:(\w+\d+)', passport),
              re.search(r'hcl:(\w+\d+)', passport)
              ]
    if all(field is not None for field in fields):
        return(
            byr_valid(int(fields[0]).group(1)) &
            iyr_valid(int(fields[1]).group(1)) &
            eyr_valid(int(fields[2]).group(1)) &
            ecl_valid(int(fields[3]).group(1)) &
            pid_valid(int(fields[4]).group(1)) &
            hcl_valid(int(fields[5]).group(1))
        )
   

with open('day4.txt') as f:
    idx = 0
    passports = ['']
    for line in f:
        if line.strip() == "":
            idx += 1
            passports.append(line.strip())
        passports[idx]+=line

total_valid_passports = 0
for passport in passports:
    # print(verify(passport))
    # total_valid_passports += verify(passport)

# print(total_valid_passports)



# # Part 1:
# #Scan input for "ecl:", "pid:", "hcl:", "byr:", "iyr:", "eyr:", "hgt:"

# def verify(passport):
#     return int(all(field in passport for field in ['byr:','iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']))

# with open('day4.txt') as f:
#     idx = 0
#     passports = ['']
#     for line in f:
#         if line.strip() == "":
#             idx += 1
#             passports.append(line)
#         passports[idx]+=line

# total_valid_passports = 0
# for passport in passports:
#     total_valid_passports += verify(passport)

# print(total_valid_passports)


# hgt_in_valid = lambda hgt: 59 <= int(input.replace('in', '')) <= 76
# hgt_cm_valid = lambda hgt: 150 <= int(input.replace('cm', '')) <= 189