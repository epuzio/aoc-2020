# Part 2:
# New idea: nested loops, 2020 - a is the two-sum for b+c

input_set = set()

with open('day1.txt') as f:
    for line in f:
        input_set.add(int(line.strip())) 

for a in input_set:
    remainder = 2020 - a
    prev_set = set()
    for b in input_set:
        if b != a: #assuming no duplicates...
            if b in prev_set:
                print(b * (2020 - a - b) * a)
            else:
                prev_set.add(remainder - b)


# Part 1:
# # Use Two-Sum - iterate through list, check hashmap of prev searches,
# # if no match, save [2020 - element] to hashmap

# prev_set = set()

# with open('day1.txt') as f:
#     for line in f:
#         num = int(line.strip())
#         if num in prev_set:
#             print(num * (2020 - num))
#             break
#         else:
#             prev_set.add(2020 - num)

