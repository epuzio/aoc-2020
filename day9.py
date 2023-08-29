preamble = 25 # number of previous numbers to check

def check_sum(nums, total): #two-sum function - repurposed from day 1
    prev = set()
    for n in nums:
        if n in prev:
            return True
        prev.add(total - n)
    return False

def invalid_num(lines): #run check_sum on each group of previous values
    prev_nums = [] # store prev values in FIFO queue, pop at end of step
    for i, line in enumerate(lines):
        prev_nums.append(int(line))
        if i >= preamble:
            if check_sum(prev_nums, int(line)) == False:
                return line
            prev_nums.pop(0)

def contiguous_range(lines, invalid_num): #finding start and end of invalid range
    start = 0 # starting index of range
    end = 0 # ending index of range
    sum = 0
    while start <= len(lines) and end <= len(lines): # O(2n) solution (pointer chasing)
        if sum < invalid_num:
            sum += int(lines[end])
            end += 1
        elif sum > invalid_num:
            sum -= int(lines[start])
            start += 1
        elif sum == invalid_num:
            return start, end

lines = open('day9.txt').readlines()
pt1 = int(invalid_num(lines))
start_idx, end_idx = contiguous_range(lines, pt1)
pt2 = lines[start_idx:end_idx]

print("Part 1:", pt1)
print("Part 2:", int(max(pt2))+int(min(pt2)))