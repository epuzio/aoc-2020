# Part 1:

import re
with open('day7.txt') as f:
    all_bags = dict() #store as inner bag -> outer bag
    bags_to_check = []
    bags_containing_shiny_gold = set()
    for line in f:
        children = []
        bag = re.match(r"(.+?) bags contain", line)[1] 
        children = re.findall(r"(\d+?) (.+?) bags?", line)
        all_bags.update({bag: children})
    for b in all_bags:
        print(all_bags[b])
        for bag in all_bags[b]:
            if 'shiny gold' == bag:
                bags_to_check.append(all_bags[b])

    print(bags_to_check)

    


        



