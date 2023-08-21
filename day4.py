# Part 2:

# Can I play Papers, Please? -> "We have Papers, Please at home"
# The Papers, Please? at home:

byr_valid = lambda year: 1920 <= year <= 2002
iyr_valid = lambda year: 2010 <= year <= 2020
eyr_valid = lambda year: 2020 <= year <= 2030
ecl_valid = lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'hzl', 'oth']
pid_valid = lambda pid: len(pid) == 9
hcl_valid = lambda hcl: re.match('^[0-9A-Fa-f]+$', hcl.replace('#', '')) and ('#' in hcl)
def hgt_valid(input):
    return(
        (59 <= int(input.replace('in', '')) <= 76) if 'in' in input else
        (150 <= int(input.replace('in', '')) <= 189) if 'cm' in input else
        False
    )
# hgt_in_valid = lambda hgt: 59 <= int(input.replace('in', '')) <= 76
# hgt_cm_valid = lambda hgt: 150 <= int(input.replace('cm', '')) <= 189


def verify(passport):
    fields = {}
    
   

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
    total_valid_passports += verify(passport)

print(total_valid_passports)



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