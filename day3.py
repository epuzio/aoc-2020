#Part 2:
def checkslope(right, down):
    line_length = 0
    num_trees = 0
    steps_right = 0

    with open('day3.txt') as f:
        l = 0
        for line in f:
            if (l % down == 0):
                line = line.strip() #strip whitespace characters
                line_length = len(line)
                if line[steps_right % line_length] == '#':
                    num_trees += 1
                steps_right += right
            l+=1
    return num_trees

total_trees = (
    checkslope(1, 1) *
    checkslope(3, 1) *
    checkslope(5, 1) *
    checkslope(7, 1) *
    checkslope(1, 2)
    )
print(total_trees)


# #Part 1:

# line_length = 0
# num_trees = 0
# steps_right = 0

# with open('day3.txt') as f:
#     for line in f:
#         line = line.strip() #strip whitespace characters
#         line_length = len(line)
#         if line[steps_right % line_length] == '#':
#             num_trees += 1
#         steps_right += 3

# print(num_trees)