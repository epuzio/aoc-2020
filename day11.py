# CONWAYS GAME OF LIFE MOMENT

with open('day11.txt') as f:
    prev_state = []
    curr_state = []
    for line in f:
        prev_state.append([])
        for c in line.strip():
            prev_state[-1].append(c)
    print(prev_state, curr_state)

    # curr_state = [[0 for _ in range(len(prev_state[0]))] for _ in range(len(prev_state))]
    # while prev_state != curr_state:
    #     for col, line in prev_state:
    #         for seat in line:
    #             neighbors = (
    #                 prev_state[col-1][seat-1] + prev_state[col-1][seat] + prev_state[col-1][seat+1] +
    #                 prev_state[col][seat -1] + prev_state[col][seat +1] +
    #                 prev_state[col+1][seat-1] + prev_state[col+1][seat] + prev_state[col+1][seat+1]
    #             )
    #             num_neighbors = neighbors.count('#')
    #             if prev_state[col][seat] == 'L' and num_neighbors == 0:
    #                 curr_state[col][seat] = '#'
    #             elif prev_state[col][seat] == '#' and num_neighbors >= 4:
    #                 curr_state[col][seat] = 'L'
    #             else:
    #                 curr_state[col][seat] = prev_state[col][seat]

      
