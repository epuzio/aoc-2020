# Part 2

with open('day6.txt') as f:
    groups = f.read().split('\n\n')
    total = 0
    for g in groups:
        s = "abcdefghijklmnopqrstuvwxyz"
        answers = g.split('\n')
        for a in answers:
            print(a)
            s = set(s) & set(a)
        total +=len(s)
    print(total)




# # Part 1

with open('day6.txt') as f: 
    groups = f.read().split('\n\n')
    total = 0
    for g in groups:
        s = set()
        for c in g.replace('\n', ''):
            s.add(c)
        total +=len(s)
    print(total)