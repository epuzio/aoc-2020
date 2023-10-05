#Part 2:

with open('day8.txt') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

instructions_list = []
for n, line in enumerate(lines):
    if 'nop' in line:
        instructions_list.append(lines[:]) # [:] creates shallow copy
        instructions_list[-1][n] = 'jmp' + line[3:]
        continue
    if 'jmp' in line:
        instructions_list.append(lines[:])
        instructions_list[-1][n] = 'nop' + line[3:]
        continue

def check_termination(instr):
    visited = set()
    idx = 0
    acc = 0
    while idx < len(instr):
        if idx in visited:
            return False, acc
        visited.add(idx)
        if 'jmp' in instr[idx]:   
            idx += int(instr[idx].split('jmp ')[1])
            continue
        if 'acc' in instr[idx]:
            acc += int(instr[idx].split('acc ')[1])
        idx+=1
    return True, acc


for l in instructions_list:
    terminates, result = check_termination(l)
    if terminates:
        print(result)


# # Part 1:
# with open('day8.txt') as f:
#     lines = []
#     for line in f:
#         lines.append(line.strip()) #def a better way to do this 

# acc = 0
# visited = set()
# idx = 0
# while True: #goddamn this is bad practice
#     if idx in visited:
#         print(acc)
#         break
#     visited.add(idx)
#     if 'jmp' in lines[idx]:   
#         idx += int(lines[idx].split('jmp ')[1])
#         continue
#     if 'acc' in lines[idx]:
#         acc += int(lines[idx].split('acc ')[1])
#     idx+=1
