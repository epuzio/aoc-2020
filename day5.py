# Part 2:
import math

def bsp(lower, upper, line):
    for c in enumerate(line):
        mid = (upper + lower) / 2
        if(c[1] == 'F' or c[1] == 'L'):
            upper = math.floor(mid)
        if(c[1] == 'B' or c[1] == 'R'):
            lower = math.ceil(mid)
    return upper

# def scan_missing(seats):
#     for i in range(len(seats)):
#         seats = sorted(seats, key=lambda x: x[0])
#         prev = sorted(seats[0])[0]
#         # print(prev)
#         for n in seats:
#             prev+=1
#             if n[0] != prev:
#                 return n
def scan_missing(seats):
    print(seats[0])
    prev = seats[0] - 1
    for s in seats:
        prev+= 1
        if s != prev:
            return s
        

with open('day5.txt') as f:
    seats = []
    for line in f:
        r = bsp(0, 127, line[0:7])
        c = bsp(0, 7, line[7:])
        seats.append((r*8) + c)
    seats = sorted(seats)
    print(seats)
    print(scan_missing(seats))
    # result = scan_missing(seats)
    # print(result)
    # print((result[0]*8)+result[1])
            




# # Part 1:

# import math

# def bsp(lower, upper, line):
#     for c in enumerate(line):
#         mid = (upper + lower) / 2
#         if(c[1] == 'F' or c[1] == 'L'):
#             upper = math.floor(mid)
#         if(c[1] == 'B' or c[1] == 'R'):
#             lower = math.ceil(mid)
#     return upper

# with open('day5.txt') as f:
#     seat_id = 0
#     for line in f:
#         row = bsp(0, 127, line[0:7])
#         column = bsp(0, 7, line[7:])
#         seat_id = max(seat_id, (row * 8) + column)
#     print(seat_id)
            

