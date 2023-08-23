with open('day6.txt') as f: #used groups strategy I saw on subreddit
    groups = f.read().split('\n\n')
    print(groups)
    total = 0
    for g in groups:
        s = set()
        for c in g.replace('\n', ''):
            s.add(c)
            print(c)
            print(s)
        total +=len(s)
        print("total: ", total) 
    print(total)










#doesnt work imma fix later tho

# with open('day6.txt') as f:
#     total = 0
#     s = set()
#     for line in f:
#         if line.strip() == '':
#             total +=len(s)
#             print("set ", s)
#             s.clear()
#         else:
#             for c in enumerate(line.strip()):
#                 print(c)
#                 s.add(c)
#         print("total: ", total)
#     total +=len(s)    
#     print(total)

