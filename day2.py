#Part 2:
num_valid = 0
with open('day2.txt') as f:
    for line in f:
        elems = line.split(" ")
        position = (map(int, elems[0].split("-")))
        count = 0
        char_to_search = elems[1][0]
        if (char_to_search == elems[2][position[0]-1]) != (char_to_search == elems[2][position[1]-1]):
            num_valid += 1
print(num_valid)




# # Part 1:
# num_valid = 0

# with open('day2.txt') as f:
#     for line in f:
#         elems = line.split(" ")
#         limit = elems[0].split("-")
#         count = 0
#         char_to_search = elems[1][0]

#         for e in range(len(elems[2])): 
#             # print("char", elems[2][e])
#             # print("count", count)
#             if elems[2][e] == char_to_search:
#                 count+=1
#         if int(limit[0]) <= count <= int(limit[1]):
#             num_valid += 1
# print(num_valid)

