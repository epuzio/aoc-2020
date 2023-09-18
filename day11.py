# CONWAYS GAME OF LIFE MOMENT
# Definitely a cleaner way to do this, but adding a 'border' of seats (labeled N) around the
# plane helps avoid out-of-bound errors w/ indexing, thank you Lokshtanov!

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

# Part 1
while True: #terrible practice, but oh well
    curr_state = [['N' for _ in range(len(prev_state[0]))] for _ in range(len(prev_state))] #initialize
    for r, row in enumerate(prev_state):
        for s, seat in enumerate(row):
            if r in range(1, len(lines[0])) and s in range(1, len(lines[0])):
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
        print("SAME")
        break
    prev_state = curr_state

print(sum(seat.count('#') for seat in prev_state))




    
