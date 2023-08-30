lines = open('day10.txt').readlines() # reading in input
lines = [int(line.strip()) for line in lines]
lines.append(0) # include the outlet (0 jolts)...
lines.append(max(lines)+3) # ...and the device adapter (max+3) in input
lines.sort()

diffs = [j-i for i, j in zip(lines[:-1], lines[1:])] #make tuple using zip, subtract difference, save to new list
print("Part 1:", diffs.count(3)*diffs.count(1))

DP_arr = [1] #list to track DP for Unique Paths
for i in range(0, max(lines)):
    DP_arr.append(0)
    for j in range(0, 3):
        if (i-j) in lines:
            DP_arr[-1] += DP_arr[i-j]
print("Part 2:", DP_arr[-1])

