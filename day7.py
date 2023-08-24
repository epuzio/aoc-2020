#good lord please come back to this

# Part 1:

import re
with open('day7.txt') as f:
    all_bags = dict()
    for line in f:
        children = []
        bag = re.match(r"(.+?) bags contain", line)[1] 
        children = re.findall(r"(\d+?) (.+?) bags?", line)
        all_bags.update({bag: children})
        # print(all_bags)
    for b in all_bags:
        print(all_bags[b])
        for _, bag in all_bags[b]:
            if 'shiny gold' == bag:
                print("yipee")

    


        



