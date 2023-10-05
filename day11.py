# Process input
lines = open('day11.txt').readlines()
prev_state = []
curr_state = []
prev_state.append(['N' for _ in range(len(lines[0])+1)]) #adding seat border
for i, line in enumerate(lines):
    prev_state.append(['N']) #seat border - clean this
    for c in line.strip():
        prev_state[-1].append(c)
    prev_state[-1].append('N') #seat border
prev_state.append(['N' for _ in range(len(lines[0])+1)]) #adding seat border

# #Part 2 (In Progress)
# def check_sides(r, s):
#     left = '.'
#     right = '.'
#     for c in prev_state[r][s:]:
#         left = c
#         if left != '.':
#             break
#     for c in prev_state[r][:s]:
#         right = c
#         if right != '.':
#             break
#     return left, right

# def check_columnns(r, s):
#     #aaa

# def check_diagonals(r, s):
#     #aaa

# while True: 
#     curr_state = [['N' for _ in range(len(prev_state[0]))] for _ in range(len(prev_state))] #initialize
#     for r, row in enumerate(prev_state):
#         for s, seat in enumerate(row):
#             if r in range(1, len(prev_state) - 1) and s in range(1, len(row) -1):
#                 neighbors = (
#                     check_sides(r, s)
#                 )
#                 num_neighbors = neighbors.count('#')
#                 if prev_state[r][s] == 'L' and num_neighbors == 0:
#                     curr_state[r][s] = '#'
#                 elif prev_state[r][s] == '#' and num_neighbors >= 5:
#                     curr_state[r][s] = 'L'
#                 else:
#                     curr_state[r][s] = prev_state[r][s]
#     if prev_state == curr_state:
#         break
#     prev_state = curr_state
# print("Part 2: ", sum(seat.count('#') for seat in prev_state))




# Part 1
while True:
    curr_state = [['N' for _ in range(len(prev_state[0]))] for _ in range(len(prev_state))] #initialize
    for r, row in enumerate(prev_state):
        for s, seat in enumerate(row):
            if r in range(1, len(prev_state) - 1) and s in range(1, len(row) -1):
                neighbors = (
                    prev_state[r-1][s-1] + prev_state[r-1][s] + prev_state[r-1][s+1] +
                    prev_state[r][s -1] + prev_state[r][s +1] +
                    prev_state[r+1][s-1] + prev_state[r+1][s] + prev_state[r+1][s+1]
                )
                num_neighbors = neighbors.count('#')
                if prev_state[r][s] == 'L' and num_neighbors == 0:
                    curr_state[r][s] = '#'
                elif prev_state[r][s] == '#' and num_neighbors >= 4:
                    curr_state[r][s] = 'L'
                else:
                    curr_state[r][s] = prev_state[r][s]
    if prev_state == curr_state:
        break
    prev_state = curr_state
print("Part 1: ", sum(seat.count('#') for seat in prev_state))