
import re #regex sweep
import math
import itertools
lines = open('day12.txt').readlines()
lines = [(line.strip()) for line in lines]

# Part 1: (may be wrong)
d = 90
man_dist = 0
directions = {0 : 1, 90 : -1, 180 : -1, 270 : 1}

for l in lines: 
    if 'F' in l:
        man_dist += int(l[1:])*(directions[d])
    if 'R' in l:
        d = (d+int(l[1:])) % 360
    if 'N' in l or 'W' in l:
        man_dist+=int(l[1:])
    if 'E' in l or 'S' in l:
        man_dist-=int(l[1:])

print("Part 1", abs(man_dist))

# Part 2:
wp = [1, 10, 0, 0]
dir = {'N': 0, 'E' : 1, 'S' : 2, 'W' : 3}
h = 0
v = 0
dir = 90
for l in lines: 
    # print(wp[dir[l[0]]])
    print(l[0])
    # n = int(l[1:])
    # if 'F' in l:
    #     h = (wp[0]*n) - (wp[2]*n)
    #     v = (wp[1]*n) - (wp[3]*n)
    # if 'R' in l: #better way to do this - save wp as list, use list slicing
    #     d = (d+l[1:]) % 90
    #     split = d / 90
    #     wp = wp[split:]+wp[:split]
    # if 'N' in l or 'W' in l or 'E' in l or 'S' in l: #better way to do this w/ list
    #     wp[dir[l[0]]]+=n
print("Part 2", abs(h)+abs(v))



