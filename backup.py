# # day 12 backup

# import re #regex sweep
# import math
# lines = open('day12.txt').readlines()
# lines = [(line.strip()) for line in lines]

# # Part 1:

# d = 90
# vertical = 0
# horizontal = 0
# directions = {0 : 1, 90 : -1, 180 : -1, 270 : 1}

# for l in lines: #there's a way to condense this but being inefficient works too
#     print(l)
#     if 'F' in l:
#         if d == 0 or d == 180:
#             vertical += int(l[1:])*(directions[d])
#         else: 
#             horizontal += int(l[1:])*(directions[d])
#     if 'R' in l:
#         d = (d+int(l[1:])) % 360
#     if 'N' in l:
#         vertical+=int(l[1:])
#     if 'E' in l:
#         horizontal-=int(l[1:])
#     if 'W' in l:
#         horizontal+=int(l[1:])
#     if 'S' in l:
#         vertical-=int(l[1:])

# print(abs(horizontal)+abs(vertical))
        











# # Experiment for part 1 that didn't go anywhere:
# # vertical = [n-s for n, s in zip(re.findall(r'N(\d+)', lines), (re.findall(r'S(\d+)', lines)))]
# # horizontal = [w-e for w, e in zip(re.findall(r'W(\d+)', lines), (re.findall(r'E(\d+)', lines)))]
# # man_dist = math.abs(vertical) + math.abs(horizontal)
# # print(man_dist)

# # lines.remove(
# #     re.search(r'^N', lines), re.search(r'^S', lines),
# #     re.search(r'^W', lines), re.search(r'^E', lines))











#----------

# import re #regex sweep
# import math
# lines = open('day12.txt').readlines()
# lines = [(line.strip()) for line in lines]

# # Part 1:

# d = 90
# man_dist = 0
# directions = {0 : 1, 90 : -1, 180 : -1, 270 : 1}

# for l in lines: #there's a way to condense this there's gotta be
#     print(man_dist)
#     if 'F' in l:
#         man_dist += int(l[1:])*(directions[d])
#     if 'R' in l:
#         d = (d+int(l[1:])) % 360
#     if 'N' in l or 'W' in l:
#         man_dist+=int(l[1:])
#     if 'E' in l or 'S' in l:
#         man_dist-=int(l[1:])

# print(abs(man_dist))
    

# Experiment for that didn't go anywhere:
# vertical = [n-s for n, s in zip(re.findall(r'N(\d+)', lines), (re.findall(r'S(\d+)', lines)))]
# horizontal = [w-e for w, e in zip(re.findall(r'W(\d+)', lines), (re.findall(r'E(\d+)', lines)))]
# man_dist = math.abs(vertical) + math.abs(horizontal)
# print(man_dist)

# lines.remove(
#     re.search(r'^N', lines), re.search(r'^S', lines),
#     re.search(r'^W', lines), re.search(r'^E', lines))